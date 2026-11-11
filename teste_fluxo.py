# -*- coding: utf-8 -*-
"""Bate na API do painel e confere o passo a passo dos DOIS fluxos.

Como rodar, SEM encostar na producao -- suba um painel de teste apontando
para uma pasta qualquer (ou para uma copia do dados.json do Y:):

    set PAINEL_PORTA=8099
    set PAINEL_SEM_NAVEGADOR=1
    set PAINEL_DADOS=C:\\temp\\painel_teste
    python servidor.py

e, noutra janela:  python teste_fluxo.py

Vale rodar tambem contra o .exe compilado (dist\\painel.exe, mesmas
variaveis): o onefile demora uns 20-30s para subir e da "conexao recusada"
antes disso -- nao e erro, e so esperar.

O teste cria chamados de mentira na pasta que o painel estiver usando.
NUNCA aponte PAINEL_DADOS para a pasta do Y:.
"""
import json
import sys
import urllib.request

BASE = 'http://127.0.0.1:8099'
ok = falhas = 0


def _post(url, body):
    req = urllib.request.Request(BASE + url, method='POST',
                                 data=json.dumps(body).encode('utf-8'),
                                 headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Recusa do passo a passo: vem como 500 com {"erro": "..."} no corpo.
        return json.loads(e.read().decode('utf-8'))


def dados():
    with urllib.request.urlopen(BASE + '/api/dados') as r:
        return json.loads(r.read().decode('utf-8'))


def checa(nome, cond, extra=''):
    global ok, falhas
    if cond:
        ok += 1
        print(f'  ok   {nome}')
    else:
        falhas += 1
        print(f'  FALHA {nome} {extra}')


def ch(id_):
    return next((c for c in dados()['chamados'] if c['id'] == id_), None)


def anda(id_, para, nota='teste', **campos):
    item = dict(campos)
    item['situacao'] = para
    return _post('/api/chamado', {'op': 'update', 'id': id_, 'item': item,
                                  'nota': nota, 'quem': 'teste'})


def novo(fluxo, **campos):
    campos['fluxo'] = fluxo
    antes = {c['id'] for c in dados()['chamados']}
    _post('/api/chamado', {'op': 'add', 'item': campos, 'quem': 'teste'})
    depois = [c for c in dados()['chamados'] if c['id'] not in antes]
    return depois[0]['id']


print('\n== 1. o que o servidor manda para a tela ==')
d = dados()
fx = d['_fluxos']
checa('dois fluxos', set(fx) == {'solicitacao', 'realizacao'}, fx.keys())
sits = {s['chave']: s for s in d['_situacoes']}
tri1 = fx['solicitacao']['trilha']
checa('fluxo 1 tem 9 passos', len(tri1) == 9, tri1)
rot = {s_['chave']: s_['rotulo'] for s_ in d['_situacoes']}
checa('passo 3 chama "Enviar peca"', rot['peca_enviada'] == 'Enviar peça', rot['peca_enviada'])
checa('passo 5 chama "Solicitar terceirizado"',
      rot['terceirizado'] == 'Solicitar terceirizado', rot['terceirizado'])
checa('passo 6 chama "Atendimento realizado?"',
      rot['concluido'] == 'Atendimento realizado?', rot['concluido'])
checa('"Atendimento realizado?" e o 6o da trilha', tri1[5] == 'concluido', tri1)
checa('a pergunta "deu certo?" mora no passo 6, nao no 5',
      len([p_ for p_ in sits['terceirizado']['proximos'] if not p_['cancela']]) == 1
      and sorted(p_['para'] for p_ in sits['concluido']['proximos'] if not p_['cancela'])
          == ['confirmar', 'enviar_peca', 'filtragem'])
checa('e ele nao pede campo nenhum', not d['_campos'].get('concluido'))
checa('fluxo 2 tem 9 passos', len(fx['realizacao']['trilha']) == 9)
checa('rotulo do parceiro no fluxo 2', fx['realizacao']['parceiro'] == 'Solicitante')
checa('rastreio obrigatorio na chegada da peca',
      any(c['campo'] == 'rastreio' and c['obrig'] for c in d['_campos'].get('peca_chegou', [])))
checa('pedido obrigatorio para ir ao ADM',
      any(c['campo'] == 'pedido' and c['obrig'] for c in d['_campos'].get('adm', [])))
checa('terceirizado oferece o campo parceiro',
      any(c['campo'] == 'parceiro' and not c['obrig'] for c in d['_campos'].get('terceirizado', [])))
checa('ao sair do cadastro de cliente pede id e cnpj',
      [c['campo'] for c in d['_campos'].get('r_equip', [])] == ['id_cliente', 'cnpj'])
checa('cancelar do fluxo 2 e o r_cancelado',
      any(p['para'] == 'r_cancelado' and p['cancela'] for p in sits['r_os']['proximos']))

print('\n== 2. fluxo 1: do cadastro ao ADM ==')
a = novo('solicitacao', os='T-100', cliente='CLIENTE TESTE', cidade='RECIFE', uf='PE')
checa('nasce no passo 1', ch(a)['situacao'] == 'filtragem')
checa('nasce carimbado com o fluxo', ch(a)['fluxo'] == 'solicitacao')
anda(a, 'enviar_peca')
anda(a, 'peca_enviada')
r = anda(a, 'peca_chegou')
checa('sem rastreio nao chega a peca', 'erro' in r, r)
checa('e continua onde estava', ch(a)['situacao'] == 'peca_enviada')
anda(a, 'peca_chegou', rastreio='AD123BR')
checa('com rastreio, passa', ch(a)['situacao'] == 'peca_chegou')
anda(a, 'terceirizado', parceiro='Maqtec - Marcos')
checa('vinculou o terceirizado', ch(a)['parceiro'] == 'Maqtec - Marcos')
r = anda(a, 'confirmar')
checa('do terceirizado nao pula a pergunta do atendimento', 'erro' in r)
anda(a, 'concluido')
checa('terceirizado solicitado -> "Atendimento realizado?"', ch(a)['situacao'] == 'concluido')
anda(a, 'confirmar')
checa('respondeu "sim": vai confirmar com o cliente', ch(a)['situacao'] == 'confirmar')
anda(a, 'pedido')
r = anda(a, 'adm')
checa('sem numero do pedido nao vai ao ADM', 'erro' in r, r)
anda(a, 'adm', pedido='PC-9988')
checa('com o pedido, encerra', ch(a)['situacao'] == 'adm')
checa('marcou a data de encerramento', bool(ch(a).get('fechado_em')))

print('\n== 3. fluxo 1: as voltas ==')
b = novo('solicitacao', os='T-200', cliente='OUTRO CLIENTE', uf='BA')
anda(b, 'terceirizado')
checa('da filtragem vai direto ao terceirizado', ch(b)['situacao'] == 'terceirizado')
anda(b, 'concluido')
checa('do terceirizado so se sai para a pergunta', ch(b)['situacao'] == 'concluido')
anda(b, 'filtragem')
checa('respondeu "nao foi realizado": volta a filtragem', ch(b)['situacao'] == 'filtragem')
anda(b, 'terceirizado')
anda(b, 'concluido')
anda(b, 'enviar_peca')
checa('respondeu "precisa de outra peca": volta ao lancamento',
      ch(b)['situacao'] == 'enviar_peca')
anda(b, 'peca_enviada')
anda(b, 'peca_chegou', rastreio='BR777')
anda(b, 'terceirizado')
anda(b, 'concluido')
anda(b, 'confirmar')
anda(b, 'filtragem')
checa('cliente disse que nao resolveu: volta a filtragem', ch(b)['situacao'] == 'filtragem')
anda(b, 'enviar_peca')
checa('o rastreio da peca anterior foi limpo', not ch(b).get('rastreio'))
checa('e o codigo antigo ficou no historico',
      any('BR777' in h['texto'] for h in ch(b)['historico']))
anda(b, 'cancelado')
checa('cancelou', ch(b)['situacao'] == 'cancelado')
anda(b, 'filtragem')
checa('reabriu', ch(b)['situacao'] == 'filtragem')

print('\n== 4. fluxo 2: do valor a nota fiscal ==')
c = novo('realizacao', cliente='EMPRESA QUE PEDIU', uf='PE', parceiro='COPYSYSTEMS')
checa('nasce em "Confirmar valores e prazo"', ch(c)['situacao'] == 'r_valores')
checa('nasce sem O.S.', not ch(c).get('os'))
r = anda(c, 'r_tecnica')
checa('nao pula do valor para a area tecnica', 'erro' in r)
anda(c, 'r_cliente')
r = anda(c, 'r_equip', id_cliente='C-55', cnpj='00.000.000/0001-00')
checa('guardou id e cnpj do cliente', ch(c).get('id_cliente') == 'C-55' and ch(c).get('cnpj','').endswith('0001-00'))
anda(c, 'r_os', serie='5JM13866', id_equip='E-900')
checa('guardou serie e id do equipamento', ch(c).get('serie') == '5JM13866')
r = anda(c, 'r_tecnica')
checa('sem numero de O.S. nao encaminha a tecnica', 'erro' in r, r)
anda(c, 'r_tecnica', os='OS-4321')
checa('com a O.S., encaminha', ch(c)['situacao'] == 'r_tecnica' and ch(c).get('os') == 'OS-4321')
anda(c, 'r_tecnica', nota='tecnico foi mas nao concluiu')
checa('"ainda nao concluiu" mantem o passo', ch(c)['situacao'] == 'r_tecnica')
checa('e a tentativa ficou no historico',
      any('nao concluiu' in h['texto'] for h in ch(c)['historico']))
anda(c, 'r_os_env')
r = anda(c, 'r_faturar')
checa('nao pula o pedido de venda', 'erro' in r)
anda(c, 'r_pedido')
checa('chegou em "Gerar pedido de venda"', ch(c)['situacao'] == 'r_pedido')
r = anda(c, 'r_faturar')
checa('sem numero do pedido de venda nao fatura', 'erro' in r, r)
anda(c, 'r_faturar', pedido_venda='PV-123')
checa('com o numero, fatura', ch(c)['situacao'] == 'r_faturar')
anda(c, 'r_nf')
checa('terminou na NF', ch(c)['situacao'] == 'r_nf')
checa('fechou a data', bool(ch(c).get('fechado_em')))
anda(c, 'r_valores')
checa('reabre no inicio do proprio fluxo', ch(c)['situacao'] == 'r_valores')

print('\n== 5. os fluxos nao se misturam ==')
e = novo('realizacao', cliente='MAIS UMA')
r = anda(e, 'filtragem')
checa('atendimento nosso nao entra no fluxo do terceirizado', 'erro' in r)
r = anda(e, 'cancelado')
checa('nem usa o cancelado do outro fluxo', 'erro' in r)
anda(e, 'r_cancelado')
checa('usa o seu', ch(e)['situacao'] == 'r_cancelado')

print('\n== 6. o lapis nao apaga o passo (bug de 03/11) ==')
f = novo('solicitacao', os='T-300', cliente='X')
anda(f, 'enviar_peca')
_post('/api/chamado', {'op': 'update', 'id': f,
                       'item': {'os': 'T-301', 'cliente': 'X', 'cidade': '', 'uf': '',
                                'parceiro': '', 'aberto_em': '', 'pedido': '',
                                'rastreio': '', 'obs': ''}})
checa('corrigir dado preserva a situacao', ch(f)['situacao'] == 'enviar_peca')
checa('e o rotulo novo nao mexeu em dado nenhum (chaves iguais)',
      all(x['situacao'] in sits for x in dados()['chamados']))
checa('e preserva o fluxo', ch(f).get('fluxo') == 'solicitacao')

print(f'\n==== {ok} ok, {falhas} falha(s) ====')
sys.exit(1 if falhas else 0)
