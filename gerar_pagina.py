"""Transforma painel.html no modulo pagina.py (que o servidor importa).

Rode depois de mexer no painel.html e antes de gerar o .exe:

    python gerar_pagina.py
"""

import os

PASTA = os.path.dirname(os.path.abspath(__file__))
ORIGEM = os.path.join(PASTA, 'painel.html')
DESTINO = os.path.join(PASTA, 'pagina.py')

html = open(ORIGEM, encoding='utf-8').read()

# A pagina vai embutida como string crua; essas duas sequencias quebrariam o literal.
for proibido in ('"""', '\\"""'):
    if proibido in html:
        raise SystemExit(f'painel.html contem {proibido!r} - ajuste o HTML antes de gerar.')
if html.endswith('\\'):
    raise SystemExit('painel.html nao pode terminar com barra invertida.')

with open(DESTINO, 'w', encoding='utf-8') as f:
    f.write('# Gerado por gerar_pagina.py a partir de painel.html. NAO EDITE A MAO.\n')
    f.write('PAGINA = r"""')
    f.write(html)
    f.write('"""\n')

print(f'pagina.py gerado ({len(html)} caracteres de HTML).')
