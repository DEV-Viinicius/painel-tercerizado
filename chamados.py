# -*- coding: utf-8 -*-
"""Modulo de CHAMADOS terceirizados.

Nasceu para tirar o acompanhamento da planilha do Google ("PLANILHA APOIO -
ATENDIMENTOS TERCEIRIZADOS", aba CHAMADOS TERCEIRIZADOS), onde o status era
texto livre (60 grafias diferentes para 332 chamados) e nao existia data
nenhuma -- nao dava para saber ha quanto tempo um chamado estava parado.

Aqui o chamado anda por um PASSO A PASSO fixo: de cada etapa so saem os
caminhos que o processo real permite, e cada mudanca vira uma linha no
historico em vez de apagar a anterior.

Nada neste arquivo toca em tecnicos ou equipamentos.
"""
import re
import unicodedata
from datetime import date, datetime

# ------------------------------------------------------------------ passos

# O painel acompanha DOIS fluxos, que nascem de pedidos opostos:
#
#   solicitacao -> NOS pedimos o atendimento a um terceirizado. E o fluxo
#                  original: quem paga e a Solivetti, e o fim da linha e o ADM.
#   realizacao  -> NOS realizamos o atendimento para outra empresa. Fluxo novo,
#                  desenhado em "Fluxo terceirizado.pdf" (11/11/2026): comeca
#                  confirmando valor e prazo e termina na nota fiscal.
#
# As chaves de passo sao UNICAS entre os dois (as do segundo levam o prefixo
# `r_`), entao UM dicionario de situacoes e UM de transicoes servem aos dois --
# so a trilha, o passo inicial e o "cancelado" e que sao por fluxo. Quem ve a
# chave sabe de que fluxo ela e, e nada precisa carregar o fluxo junto.

# chave -> (rotulo na tela, cor, ainda esta na sua mao?)
SITUACOES = {
    # ---- fluxo 1: pedimos atendimento a um terceirizado ----
    'filtragem':    ('Solicitar filtragem',       '#6b7a90', True),
    'enviar_peca':  ('Lançar peça no sistema',    '#d08a00', True),
    'peca_enviada': ('Enviar peça',               '#8a4fd0', True),
    'peca_chegou':  ('Peça chegou',               '#b05fa0', True),
    'terceirizado': ('Solicitar terceirizado',    '#2f6fd0', True),
    # So uma confirmacao de que o atendimento aconteceu, antes de ligar para o
    # cliente. A chave continua `concluido` (era "Atendimento concluido"), por
    # isso nenhum chamado precisou ser migrado quando o rotulo mudou.
    'concluido':    ('Atendimento realizado?',    '#1f9254', True),
    'confirmar':    ('Confirmar com o cliente',   '#0f8f8f', True),
    'pedido':       ('Gerar pedido de compra',    '#c85a00', True),
    'adm':          ('Enviado ao ADM',            '#4a5568', False),
    'cancelado':    ('Cancelado',                 '#99a3b0', False),

    # ---- fluxo 2: nos realizamos o atendimento ----
    # Cada rotulo diz o que FALTA fazer -- e assim que a fila e lida: quem esta
    # em "Gerar O.S." ainda nao gerou. O ultimo e o unico no passado: acabou.
    'r_valores':    ('Confirmar valores e prazo',    '#6b7a90', True),
    'r_cliente':    ('Cadastrar cliente',            '#0f8f8f', True),
    'r_equip':      ('Cadastrar equipamento',        '#2f6fd0', True),
    'r_os':         ('Gerar O.S.',                   '#8a4fd0', True),
    'r_tecnica':    ('Encaminhado à área técnica',   '#d08a00', True),
    'r_os_env':     ('Enviar O.S. preenchida',       '#b05fa0', True),
    'r_pedido':     ('Gerar pedido de venda',        '#c85a00', True),
    'r_faturar':    ('Faturar pedido',               '#1f9254', True),
    'r_nf':         ('NF enviada',                   '#4a5568', False),
    'r_cancelado':  ('Cancelado',                    '#99a3b0', False),
}

FLUXOS = {
    'solicitacao': {
        'rotulo':    'Chamados terceirizados',
        'sub':       'atendimento que NÓS pedimos a um terceirizado',
        # como chamar, nesse fluxo, a empresa/pessoa do outro lado
        'parceiro':  'Parceiro / terceirizado',
        'trilha':    ['filtragem', 'enviar_peca', 'peca_enviada', 'peca_chegou',
                      'terceirizado', 'concluido', 'confirmar', 'pedido', 'adm'],
        'cancelado': 'cancelado',
    },
    'realizacao': {
        'rotulo':    'Atendimentos que realizamos',
        'sub':       'atendimento que OUTRA empresa pede para nós',
        'parceiro':  'Solicitante',
        'trilha':    ['r_valores', 'r_cliente', 'r_equip', 'r_os', 'r_tecnica',
                      'r_os_env', 'r_pedido', 'r_faturar', 'r_nf'],
        'cancelado': 'r_cancelado',
    },
}

FLUXO_PADRAO = 'solicitacao'
PADRAO = {f: c['trilha'][0] for f, c in FLUXOS.items()}
TRILHAS = {f: c['trilha'] for f, c in FLUXOS.items()}
# De que fluxo e cada passo. O 'concluido' aposentado entra junto, senao um
# chamado antigo ficaria sem fluxo nenhum.
DE_QUE_FLUXO = {k: f for f, c in FLUXOS.items() for k in c['trilha']}
DE_QUE_FLUXO.update({c['cancelado']: f for f, c in FLUXOS.items()})

SIT_PADRAO = PADRAO[FLUXO_PADRAO]
ABERTAS = [k for k, v in SITUACOES.items() if v[2]]
TRILHA = TRILHAS[FLUXO_PADRAO]
FINAL = TRILHA[-1]


def fluxo_de(sit):
    """A que fluxo pertence esse passo (ou esse chamado)."""
    if isinstance(sit, dict):
        return sit.get('fluxo') or DE_QUE_FLUXO.get(sit.get('situacao'), FLUXO_PADRAO)
    return DE_QUE_FLUXO.get(sit, FLUXO_PADRAO)

# De cada passo, PARA ONDE da para ir -- e com que palavras o botao convida.
# O que nao esta aqui o servidor recusa: o passo a passo e para valer.
TRANSICOES = {
    'filtragem': [
        ('enviar_peca',  'Filtragem OK — precisa de peça'),
        ('terceirizado', 'Não resolveu / não precisa de peça — solicitar terceirizado'),
    ],
    'enviar_peca': [
        ('peca_enviada', 'Peça lançada no sistema'),
    ],
    'peca_enviada': [
        ('peca_chegou', 'Peça enviada e chegou no cliente'),
    ],
    'peca_chegou': [
        ('terceirizado', 'Solicitar atendimento ao terceirizado'),
    ],
    'terceirizado': [
        ('concluido', 'Terceirizado solicitado — aguardando o atendimento'),
    ],
    # E AQUI que o caminho se divide: o passo e uma pergunta ("o atendimento
    # foi realizado?"), entao e aqui que a caixa oferece as respostas.
    'concluido': [
        ('confirmar',   'Sim, atendimento realizado — confirmar com o cliente'),
        # Nao foi realizado: o chamado recomeca, porque e preciso filtrar de
        # novo para saber o que fazer.
        ('filtragem',   'Não foi realizado — voltar à filtragem'),
        # Caso diferente: o terceirizado ATENDEU, so que descobriu que precisa
        # de outra peca. Ai volta para o lancamento, nao para a filtragem --
        # e o chamado pode dar essa volta quantas vezes precisar.
        ('enviar_peca', 'Atendeu mas precisa de outra peça — lançar peça'),
    ],
    'confirmar': [
        ('pedido',    'Cliente confirmou — gerar pedido de compra'),
        ('filtragem', 'Cliente diz que não resolveu — voltar à filtragem'),
    ],
    'pedido': [
        ('adm', 'Pedido enviado ao ADM para pagamento'),
    ],
    # Fim da linha e cancelado so saem reabrindo.
    'adm': [
        ('filtragem', 'Reabrir chamado'),
    ],
    'cancelado': [
        ('filtragem', 'Reabrir chamado'),
    ],

    # ---- fluxo 2: nos realizamos o atendimento ----
    'r_valores': [
        ('r_cliente', 'Cliente confirmou valor e prazo'),
    ],
    'r_cliente': [
        ('r_equip', 'Cliente cadastrado — cadastrar o equipamento'),
    ],
    'r_equip': [
        ('r_os', 'Equipamento cadastrado — gerar a O.S.'),
    ],
    'r_os': [
        ('r_tecnica', 'O.S. gerada — encaminhar à área técnica'),
    ],
    'r_tecnica': [
        ('r_os_env', 'Atendimento concluído — enviar O.S. preenchida'),
        # O "nao" do fluxograma: o atendimento nao fechou, o chamado fica onde
        # esta e a tentativa vira uma linha no historico.
        ('r_tecnica', 'Ainda não concluiu — continua com a área técnica'),
    ],
    'r_os_env': [
        ('r_pedido', 'O.S. enviada — gerar pedido de venda'),
    ],
    'r_pedido': [
        ('r_faturar', 'Pedido de venda gerado — faturar'),
    ],
    'r_faturar': [
        ('r_nf', 'Pedido faturado e NF enviada'),
    ],
    'r_nf': [
        ('r_valores', 'Reabrir atendimento'),
    ],
    'r_cancelado': [
        ('r_valores', 'Reabrir atendimento'),
    ],
}

# Campos que a caixa de andamento pede numa passagem de passo.
# passo -> [(campo, rotulo)] -- EXIGE recusa em branco, OFERECE so mostra.
#
# Os dois sao indexados pelo passo de DESTINO, e e por isso que o campo
# aparece na SAIDA do passo que o produz: quem esta em "Gerar O.S." so tem o
# numero da O.S. na hora de dizer que gerou. Pedir na entrada seria pedir
# antes de existir.
EXIGE = {
    # Rastreio voltou a ser obrigatorio (documentacao de 11/11/2026). Sai de
    # "Peca enviada": e na conferencia da entrega que o codigo esta em maos.
    'peca_chegou': [('rastreio', 'Código de rastreio')],
    # Sai de "Gerar pedido de compra": sem o numero o ADM nao tem o que pagar.
    'adm':         [('pedido', 'Número do pedido de compra')],
    # Fluxo 2: sai de "Gerar O.S." e de "Gerar pedido de venda".
    'r_tecnica':   [('os', 'Número da O.S.')],
    'r_faturar':   [('pedido_venda', 'Número do pedido de venda')],
}


OFERECE = {
    # "Vincular chamado ao terceirizado": na hora de mandar para o parceiro e
    # que se sabe quem vai atender. Nao trava -- as vezes ainda e "a definir".
    'terceirizado': [('parceiro', 'Terceirizado que vai atender')],
    # Fluxo 2: saem de "Cadastrar cliente" e de "Cadastrar equipamento".
    'r_equip':      [('id_cliente', 'ID do cliente'), ('cnpj', 'CNPJ do cliente')],
    'r_os':         [('serie', 'Série do equipamento'), ('id_equip', 'ID do equipamento')],
}


def campos_do_passo(para):
    """[(campo, rotulo, obrigatorio)] que a caixa de andamento mostra."""
    return ([(c, r, True) for c, r in EXIGE.get(para, [])] +
            [(c, r, False) for c, r in OFERECE.get(para, [])])


# Campos que ZERAM ao entrar num passo. Voltando ao lancamento da peca, o
# rastreio da peca ANTERIOR nao pode ficar no campo fingindo ser o da nova.
# O codigo antigo vai para o historico antes de sair.
# campo -> (como chamar o campo no historico)
LIMPA_AO_ENTRAR = {
    'enviar_peca': [('rastreio', 'Rastreio da peça anterior')],
}


def falta_para(para, ch):
    """Nome do 1o campo obrigatorio vazio para ir ao passo `para`, ou None."""
    for campo, nome in EXIGE.get(para, []):
        if not str(ch.get(campo) or '').strip():
            return nome
    return None


# Cancelar vale em qualquer etapa que ainda esteja na sua mao: equipamento que
# vai ser substituido ou retirado nao percorre o fluxo ate o fim.
# passo -> o "cancelado" DO FLUXO dele (cada fluxo tem o seu, senao reabrir um
# atendimento nosso cairia na filtragem do outro fluxo).
CANCELAVEIS = {}
for _f, _c in FLUXOS.items():
    for _k in _c['trilha'][:-1]:
        CANCELAVEIS[_k] = _c['cancelado']
CANCELADOS = {c['cancelado'] for c in FLUXOS.values()}


def pode_ir(de, para):
    """A mudanca de passo e permitida pelo processo?"""
    if de == para:
        return True
    if para in CANCELADOS:
        return CANCELAVEIS.get(de) == para
    return para in [p for p, _ in TRANSICOES.get(de, [])]


def proximos(de):
    """Lista [(passo, texto do botao)] que a tela deve oferecer."""
    saidas = list(TRANSICOES.get(de, []))
    if de in CANCELAVEIS:
        saidas.append((CANCELAVEIS[de], 'Cancelar chamado'))
    return saidas


def migrar(dados):
    """Poe chamado gravado por versao antiga no formato de hoje. Devolve quantos mexeu.

    Hoje so falta uma coisa: dizer de que fluxo o chamado e. Quem nao tem o
    campo nasceu antes dos dois fluxos existirem, entao e do original.
    Os rotulos que mudaram em 11/11/2026 ("Peca enviada" -> "Enviar peca",
    "Enviado ao terceirizado" -> "Solicitar terceirizado", "Atendimento
    concluido" -> "Atendimento realizado?") nao precisam de migracao: as
    CHAVES continuam as mesmas, so o texto na tela mudou.
    """
    n = 0
    for ch in dados.get('chamados', []):
        if not ch.get('fluxo'):
            ch['fluxo'] = fluxo_de(ch.get('situacao'))
            n += 1
    return n


def _nrm(s):
    """Maiusculas, sem acento, sem pontuacao. Para comparar texto baguncado."""
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return ' '.join(re.sub(r'[^A-Z0-9 ]', ' ', s.upper()).split())


# A ordem IMPORTA: vence a primeira que casar.
# Montada em cima dos 60 status reais que existiam na planilha.
_REGRAS = [
    # Antes de tudo: texto que diz que o atendimento NAO resolveu, mesmo
    # contendo a palavra "atendido". Ex.: "ATENDIDO MAS IMPRESSAO CONTINUA EM BRANCO".
    (r'SEM SUCESSO|MAS IMPRESSAO|CONTINUA EM BRANCO', 'filtragem'),
    (r'CANCELAD', 'cancelado'),
    # Na planilha "CONCLUIDO" era fim de linha -- o chamado ja tinha passado por
    # tudo, inclusive pedido de compra. Por isso entra no fim do fluxo, e nao em
    # "atendimento concluido": senao 288 chamados encerrados voltariam para a
    # fila pedindo confirmacao com o cliente.
    (r'CONCLU|CONLUIDO|FINALIZAD|RESOLVID|ATENDIDO POR|INSTALADO PELO CLIENTE|'
     r'CHAMADO ATENDIDO|REALIZADO A TROCA', 'adm'),
    # Orcamento/aprovacao e espera para poder mandar a peca.
    (r'ORCAMENTO|APROVACAO', 'enviar_peca'),
    (r'AGUARDANDO.*PEC|COMPRA DE PECA|CHEGADA DE PEC', 'enviar_peca'),
    (r'PECA ENVIADA|ENVIAR PECA|PECA NO CLIENTE|PECA PARA', 'peca_enviada'),
    (r'ENVIADO|ENCAMINHADO|WHATSAPP|EMAIL', 'terceirizado'),
]


def classificar(texto):
    """Texto livre do status antigo -> em que passo o chamado entra."""
    t = _nrm(texto)
    if not t:
        return SIT_PADRAO
    for padrao, sit in _REGRAS:
        if re.search(padrao, t):
            return sit
    return SIT_PADRAO


# ------------------------------------------------------- cidade / UF

# Clientes como "FIORI MARANHAO" ou "LOGPLACE SERGIPE" trazem o ESTADO no nome,
# nao a cidade. Sem isto eles ficariam sem UF nenhuma.
_ESTADOS = {
    'ACRE': 'AC', 'ALAGOAS': 'AL', 'AMAPA': 'AP', 'AMAZONAS': 'AM', 'BAHIA': 'BA',
    'CEARA': 'CE', 'DISTRITO FEDERAL': 'DF', 'ESPIRITO SANTO': 'ES', 'GOIAS': 'GO',
    'MARANHAO': 'MA', 'MATO GROSSO': 'MT', 'MATO GROSSO DO SUL': 'MS',
    'MINAS GERAIS': 'MG', 'PARA': 'PA', 'PARAIBA': 'PB', 'PARANA': 'PR',
    'PERNAMBUCO': 'PE', 'PIAUI': 'PI', 'RIO DE JANEIRO': 'RJ',
    'RIO GRANDE DO NORTE': 'RN', 'RIO GRANDE DO SUL': 'RS', 'RONDONIA': 'RO',
    'RORAIMA': 'RR', 'SANTA CATARINA': 'SC', 'SAO PAULO': 'SP',
    'SERGIPE': 'SE', 'TOCANTINS': 'TO',
}


def indice_cidades(equipamentos):
    """Monta {cidade normalizada: UF} a partir dos equipamentos que o painel ja tem.

    No cadastro de equipamentos a cidade vem como "SALVADOR (BA)" -- o
    parenteses precisa sair, senao nada casa.
    """
    cont = {}
    for e in equipamentos:
        uf = (e.get('uf') or '').strip().upper()
        if not uf or uf == '--':
            continue
        cid = _nrm(re.sub(r'\(.*?\)', ' ', str(e.get('cidade') or '')))
        if len(cid) > 3:
            cont.setdefault(cid, {})
            cont[cid][uf] = cont[cid].get(uf, 0) + 1
    # cidade homonima em 2 estados: fica com o estado que tem mais equipamentos
    return {c: max(ufs.items(), key=lambda x: x[1])[0] for c, ufs in cont.items()}


def deduzir_local(cliente, idx_cidades):
    """Descobre (cidade, UF) a partir do nome do cliente.

    A planilha nunca teve coluna de cidade: ela mora dentro do nome
    ("FIORI SALVADOR", "RCR SAO LUIS"). Devolve ('', '') quando o nome e so
    razao social ("SAO BRAZ S/A") -- ai alguem preenche a mao no painel.
    """
    n = _nrm(cliente)
    if not n:
        return '', ''
    # nome de estado por extenso (mais longo primeiro: "MATO GROSSO DO SUL" antes de "MATO GROSSO")
    for nome in sorted(_ESTADOS, key=len, reverse=True):
        if re.search(r'\b' + re.escape(nome) + r'\b', n):
            return '', _ESTADOS[nome]
    # nome de cidade que o painel ja conhece (mais longa primeiro:
    # "SAO LUIS" antes de "SAO", "JUAZEIRO DO NORTE" antes de "JUAZEIRO")
    for cid in sorted(idx_cidades, key=len, reverse=True):
        if re.search(r'\b' + re.escape(cid) + r'\b', n):
            return cid, idx_cidades[cid]
    return '', ''


# ------------------------------------------------------------- historico

def anotar(ch, texto, quem='painel'):
    """Acrescenta uma linha ao historico do chamado, sem apagar as anteriores."""
    if not texto:
        return
    ch.setdefault('historico', []).append({
        'em': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'quem': quem,
        'texto': str(texto).strip(),
    })


def dias_parado(ch, hoje=None):
    """Dias desde a abertura (ou ate o encerramento). None quando falta a data."""
    ini = (ch.get('aberto_em') or '').strip()
    if not ini:
        return None
    try:
        d0 = datetime.strptime(ini[:10], '%Y-%m-%d').date()
    except ValueError:
        return None
    fim = (ch.get('fechado_em') or '').strip()
    if fim:
        try:
            d1 = datetime.strptime(fim[:10], '%Y-%m-%d').date()
        except ValueError:
            d1 = hoje or date.today()
    else:
        d1 = hoje or date.today()
    return max(0, (d1 - d0).days)


# ----------------------------------------------------------- importacao

_CAB = {
    'os': ('OS', 'O.S', 'CHAMADO', 'NUMERO'),
    'cliente': ('CLIENTE',),
    'status': ('STATUS', 'SITUACAO', 'ANDAMENTO'),
    'parceiro': ('PARCEIRO', 'TERCEIRIZADO', 'EMPRESA'),
    'rastreio': ('RASTREIO', 'RASTREAMENTO', 'CODIGO'),
    'pedido': ('PEDIDO',),
}


def _mapear(headers):
    """Acha em que coluna esta cada campo, pelo nome do cabecalho."""
    idx = {}
    for i, h in enumerate(headers):
        hn = _nrm(h)
        if not hn:
            continue
        for campo, apelidos in _CAB.items():
            if campo in idx:
                continue
            if any(hn == a or hn.startswith(a + ' ') or hn == a.replace('.', '') for a in apelidos):
                idx[campo] = i
    return idx


def _texto(v):
    """Celula -> texto. O Excel entrega numero de OS como 79119.0."""
    if v is None:
        return ''
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    if isinstance(v, (datetime, date)):
        return v.strftime('%Y-%m-%d')
    return str(v).strip()


def ler_planilha(caminho, aba='CHAMADOS TERCEIRIZADOS'):
    """Le a aba de chamados do .xlsx e devolve uma lista de dicionarios crus."""
    import openpyxl
    wb = openpyxl.load_workbook(caminho, read_only=True, data_only=True)
    if aba not in wb.sheetnames:
        raise ValueError(f'A planilha nao tem a aba "{aba}". Abas: {wb.sheetnames}')
    ws = wb[aba]

    linhas = [list(r) for r in ws.iter_rows(values_only=True)]
    # A linha 1 e o titulo com a logo; o cabecalho de verdade e a primeira
    # linha que tiver "OS" e "CLIENTE".
    pos_cab = None
    for i, linha in enumerate(linhas[:10]):
        vals = [_nrm(c) for c in linha]
        if 'OS' in vals and 'CLIENTE' in vals:
            pos_cab = i
            break
    if pos_cab is None:
        raise ValueError('Nao achei o cabecalho (uma linha com "OS" e "CLIENTE").')

    idx = _mapear(linhas[pos_cab])
    faltando = [c for c in ('os', 'cliente') if c not in idx]
    if faltando:
        raise ValueError(f'Faltam colunas na planilha: {", ".join(faltando)}')

    out = []
    for linha in linhas[pos_cab + 1:]:
        reg = {campo: _texto(linha[i]) if i < len(linha) else ''
               for campo, i in idx.items()}
        if not any(reg.values()):
            continue
        out.append(reg)
    return out


def importar(caminho, equipamentos, novo_id, aba='CHAMADOS TERCEIRIZADOS'):
    """Planilha -> lista de chamados prontos para entrar no dados.json.

    `novo_id` e a funcao de id do servidor, para os ids seguirem a mesma serie.
    Devolve (chamados, relatorio).
    """
    crus = ler_planilha(caminho, aba)
    idx_cid = indice_cidades(equipamentos)

    # A mesma O.S. aparece mais de uma vez na planilha: como la nao dava para
    # atualizar um chamado sem apagar o texto anterior, as pessoas lancavam uma
    # linha nova. Aqui as linhas da mesma O.S. viram UM chamado -- a ultima
    # manda nos campos (e a mais recente) e as anteriores entram no historico.
    grupos = {}
    for i, c in enumerate(crus):
        os_ = str(c.get('os', '')).strip()
        chave = ('os', os_) if os_ else ('linha', i)
        grupos.setdefault(chave, []).append(c)

    chamados = []
    rel = {'lidos': len(crus), 'por_situacao': {}, 'sem_uf': 0,
           'sem_data': 0, 'fundidos': 0}
    for linhas in grupos.values():
        c = linhas[-1]
        cidade, uf = deduzir_local(c.get('cliente'), idx_cid)
        status_antigo = c.get('status', '')
        sit = classificar(status_antigo)

        ch = {
            'id': novo_id('c'),
            'os': c.get('os', ''),
            'cliente': c.get('cliente', ''),
            'cidade': cidade,
            'uf': uf,
            'parceiro': c.get('parceiro', ''),
            'fluxo': 'solicitacao',
            'situacao': sit,
            'rastreio': c.get('rastreio', ''),
            'pedido': c.get('pedido', ''),
            # A planilha de origem NAO tinha data nenhuma. Nao da para inventar:
            # fica vazio e o painel mostra "sem data" ate alguem preencher.
            'aberto_em': '',
            'fechado_em': '',
            'obs': status_antigo,
            'historico': [],
        }
        # Historico em ordem: as linhas antigas primeiro, a atual por ultimo.
        for ant in linhas[:-1]:
            txt = (ant.get('status') or '').strip()
            quem_ant = (ant.get('parceiro') or '').strip()
            if txt or quem_ant:
                anotar(ch, f'(lancamento anterior na planilha{" - " + quem_ant if quem_ant else ""}) '
                           f'{txt or "sem status"}', quem='planilha')
        if status_antigo:
            anotar(ch, status_antigo, quem='planilha')
        if len(linhas) > 1:
            rel['fundidos'] += len(linhas) - 1
        chamados.append(ch)

        rel['por_situacao'][sit] = rel['por_situacao'].get(sit, 0) + 1
        if not uf:
            rel['sem_uf'] += 1
        rel['sem_data'] += 1

    rel['importados'] = len(chamados)
    return chamados, rel
