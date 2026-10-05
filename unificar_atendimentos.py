"""
Leitura das planilhas de origem do PAINEL DE ATENDIMENTOS.

Origem:
 - Relatorio Equipamentos - Completo.xls / .xlsx (equipamentos / series)
 - PLANILHA APOIO - ATENDIMENTOS TERCEIRIZADOS (1).xlsx (terceirizados)

OBS: este modulo foi RECONSTRUIDO a partir do bytecode do painel.exe
(o servidor.py e o unificar_atendimentos.py originais foram apagados da
pasta TERCERIZADO). As funcoes usadas pelo painel -- norm, limpa,
ler_terceirizados e ler_equipamentos -- estao identicas ao original.
As funcoes casar() e main(), que geravam a planilha
"ATENDIMENTOS UNIFICADO.xlsx" e nunca sao chamadas pelo painel, nao
foram reconstruidas; o bytecode original delas continua guardado em
C:\\Claude\\build\\painel\\painel\\PYZ-00.pyz caso um dia facam falta.
"""

import os
import re
import unicodedata

import openpyxl
import xlrd

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQ_TERC = os.path.join(PASTA, 'PLANILHA APOIO - ATENDIMENTOS TERCEIRIZADOS (1).xlsx')
ARQ_EQUIP = os.path.join(PASTA, 'Relatório Equipamentos - Completo.xls')
ARQ_EQUIP_XLSX = os.path.join(PASTA, 'Relatório Equipamentos - Completo.xlsx')
ARQ_SAIDA = os.path.join(PASTA, 'ATENDIMENTOS UNIFICADO.xlsx')


def norm(s):
    """Texto comparavel: sem acento, sem (parenteses), espacos unicos, MAIUSCULO."""
    if s is None:
        return ''
    s = str(s).replace('\ufffd', '').replace('\ufffd', '')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\s+', ' ', s).strip().upper()
    return s


def limpa(s):
    """Texto exibivel: so tira espacos repetidos das pontas."""
    if s is None:
        return ''
    s = str(s).replace('\ufffd', '').replace('\ufffd', '')
    return re.sub(r'\s+', ' ', s).strip()


def ler_terceirizados():
    """Le a planilha de terceirizados. A UF fica em linha de bloco e vale ate mudar."""
    ws = openpyxl.load_workbook(ARQ_TERC, read_only=True, data_only=True).active
    rows = list(ws.iter_rows(values_only=True))

    terc = []
    uf_atual = None
    for r in rows[2:]:
        r = (list(r) + [None] * 11)[:11]
        uf, local, nome, contato, email, ddd, tel, valor, ret, desl, obs = r
        if uf:
            uf_atual = str(uf).strip()
        if not nome:
            continue

        ddd_s = limpa(ddd)
        tel_s = limpa(tel)
        telefone = f'({ddd_s}) {tel_s}'.strip() if tel_s else ddd_s

        partes = []
        if limpa(obs):
            partes.append(limpa(obs))
        if limpa(ret):
            partes.append(f'Retorno: {limpa(ret)}')
        if limpa(desl):
            partes.append(f'Deslocamento: {limpa(desl)}')

        terc.append({
            'uf': norm(uf_atual),
            'local': norm(local),
            'nome': limpa(nome),
            'valor': limpa(valor),
            'contato': limpa(contato),
            'email': limpa(email),
            'telefone': telefone,
            'obs': ' | '.join(partes),
        })
    return terc


def ler_equipamentos():
    """Le a planilha de equipamentos (prefere o .xlsx; cai para o .xls antigo)."""
    equip = []
    if os.path.exists(ARQ_EQUIP_XLSX):
        ws = openpyxl.load_workbook(ARQ_EQUIP_XLSX, read_only=True, data_only=True).active
        for r in list(ws.iter_rows(values_only=True))[1:]:
            equip.append([limpa(x) for x in r])
    else:
        sh = xlrd.open_workbook(ARQ_EQUIP).sheet_by_index(0)
        for i in range(1, sh.nrows):
            equip.append([limpa(x) for x in sh.row_values(i)])
    return equip
