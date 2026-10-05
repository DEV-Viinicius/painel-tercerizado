"""Gera o painel.exe e publica na pasta de rede.

    python publicar.py           gera o exe e publica no Y:
    python publicar.py --teste   so gera o exe (nao publica nada)

Faz na ordem certa: pagina -> exe -> rar -> backup da versao anterior ->
publicacao. Para tudo e avisa se o painel estiver aberto, porque o Windows
nao deixa trocar um .exe que esta rodando.

A equipe baixa um .rar (a pasta de rede bloqueia .exe por regra de TI, mas
aceita .rar). Se o WinRAR nao estiver instalado, o script avisa e para.
"""

import os
import shutil
import socket
import subprocess
import sys
from datetime import date

PASTA = os.path.dirname(os.path.abspath(__file__))
REDE = r'Y:\DOCUMENTACOES E TUTORIAIS\Projetos de Setores\Tercerizado'
REDE_UNC = r'\\192.168.0.5\Tecnologia\DOCUMENTACOES E TUTORIAIS\Projetos de Setores\Tercerizado'
EXE_LOCAL = r'C:\Users\suporte06\Desktop\TERCERIZADO\painel.exe'
PACOTE = 'PainelAtendimentos.rar'
RARS = (r'C:\Program Files\WinRAR\rar.exe', r'C:\Program Files (x86)\WinRAR\rar.exe')
TESTE = '--teste' in sys.argv


def achar_rar():
    for c in RARS:
        if os.path.exists(c):
            return c
    return None


def passo(txt):
    print(f'\n>> {txt}')


def painel_aberto():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.settimeout(0.4)
    try:
        c.connect(('127.0.0.1', 8000))
        return True
    except OSError:
        return False
    finally:
        c.close()


def achar_rede():
    for c in (REDE, REDE_UNC):
        if os.path.isdir(c):
            return c
    return None


def main():
    os.chdir(PASTA)

    if painel_aberto():
        print('\nO painel esta ABERTO na porta 8000.')
        print('Feche com o atalho "Parar Painel" e rode de novo.')
        return 1

    rar = achar_rar()
    if not rar:
        print('\nNao achei o WinRAR (rar.exe) nestes caminhos:')
        for c in RARS:
            print('  ', c)
        print('Instale o WinRAR ou ajuste RARS no topo deste arquivo.')
        return 1

    passo('Gerando pagina.py a partir do painel.html')
    subprocess.run([sys.executable, 'gerar_pagina.py'], check=True)

    passo('Compilando o painel.exe (demora ~1 minuto)')
    for lixo in ('build', 'dist', 'painel.spec'):
        if os.path.isdir(lixo):
            shutil.rmtree(lixo, ignore_errors=True)
        elif os.path.isfile(lixo):
            os.remove(lixo)
    subprocess.run([sys.executable, '-m', 'PyInstaller', '--onefile', '--noconsole',
                    '--name', 'painel', 'servidor.py'], check=True)

    exe = os.path.join(PASTA, 'dist', 'painel.exe')
    if not os.path.exists(exe):
        print('ERRO: o exe nao foi gerado.')
        return 1
    print(f'   exe gerado: {os.path.getsize(exe) / 1024 / 1024:.1f} MB')

    passo(f'Montando o {PACOTE}')
    pacote_novo = os.path.join(PASTA, 'dist', PACOTE)
    if os.path.exists(pacote_novo):
        os.remove(pacote_novo)
    # -ep guarda so o nome do arquivo (sem a pasta), -m3 compressao normal
    r = subprocess.run([rar, 'a', '-ep', '-m3', '-y', pacote_novo, exe],
                       capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(pacote_novo):
        print('ERRO ao gerar o .rar:', (r.stdout or '') + (r.stderr or ''))
        return 1
    # confere que o que entrou no pacote e mesmo o exe recem-compilado
    if subprocess.run([rar, 't', pacote_novo], capture_output=True).returncode != 0:
        print('ERRO: o .rar gerado nao passou no teste de integridade.')
        return 1
    print(f'   {PACOTE}: {os.path.getsize(pacote_novo) / 1024 / 1024:.1f} MB (integridade OK)')

    if TESTE:
        print('\n--teste: parei por aqui. Nada foi publicado.')
        print(f'O exe esta em {exe}')
        return 0



    rede = achar_rede()
    if not rede:
        print('\nNao achei a pasta de rede. Publicacao cancelada (o exe esta pronto em dist\\).')
        return 1

    passo('Guardando a versao anterior em _versao_anterior\\')
    backup = os.path.join(rede, '_versao_anterior')
    os.makedirs(backup, exist_ok=True)
    atual = os.path.join(rede, PACOTE)
    if os.path.exists(atual):
        destino = os.path.join(backup, f'PainelAtendimentos_ANTIGO_{date.today()}.rar')
        shutil.copy2(atual, destino)
        print(f'   {os.path.basename(destino)}')

    passo('Publicando na rede e neste PC')
    shutil.copy2(pacote_novo, atual)
    print(f'   {atual}')
    if os.path.isdir(os.path.dirname(EXE_LOCAL)):
        shutil.copy2(exe, EXE_LOCAL)
        print(f'   {EXE_LOCAL}')

    manual = os.path.join(PASTA, 'COMO ACESSAR.txt')
    if os.path.exists(manual):
        shutil.copy2(manual, os.path.join(rede, 'COMO ACESSAR.txt'))
        print(f'   COMO ACESSAR.txt atualizado')

    print(f'\nPronto. Quem usa o painel em outra maquina precisa fechar o painel,')
    print(f'baixar o {PACOTE} do Y:, extrair e substituir o painel.exe.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
