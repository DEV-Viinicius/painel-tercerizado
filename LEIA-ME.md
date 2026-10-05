# Painel de Atendimentos Terceirizados

Painel web que mostra, por estado, os **equipamentos** (séries) e os **técnicos
terceirizados** que atendem cada localidade.

**Esta pasta é a única cópia do código-fonte. Não apague.**

---

## Como funciona

Não existe um "PC servidor". **Cada pessoa roda o `painel.exe` na própria
máquina**, e o programa sobe um servidor que só ela enxerga
(`127.0.0.1:8000` — não aparece na rede, não precisa de firewall).

O que é compartilhado é **um único arquivo de dados na pasta de rede**:

```
Y:\DOCUMENTACOES E TUTORIAIS\Projetos de Setores\Tercerizado\
   ├── dados.json          <- a base de verdade, todos leem e gravam aqui
   ├── dados.json.lock     <- trava criada só no instante de gravar
   ├── PainelAtendimentos.rar  <- o que a equipe baixa
   ├── COMO ACESSAR.txt        <- manual do usuário final
   ├── LOGO SOLIVETTI.jpg
   ├── Parar Painel.vbs
   ├── PLANILHA APOIO - ATENDIMENTOS TERCEIRIZADOS (1).xlsx   <- NÃO APAGUE
   ├── Relatório Equipamentos - Completo.xlsx                 <- NÃO APAGUE
   └── _versao_anterior\   <- só rollback de emergência
```

    PC do João       PC da Maria      PC do Pedro
    painel.exe       painel.exe       painel.exe
    localhost:8000   localhost:8000   localhost:8000
         └────────────────┴────────────────┘
                todos no mesmo dados.json

**Onde o programa procura os dados**, nesta ordem — usa a primeira que existir:

1. a variável de ambiente `PAINEL_DADOS` (serve para testar sem tocar na rede)
2. `\\192.168.0.5\Tecnologia\DOCUMENTACOES E TUTORIAIS\Projetos de Setores\Tercerizado`
3. `Y:\DOCUMENTACOES E TUTORIAIS\Projetos de Setores\Tercerizado`
4. **a pasta do próprio .exe** — se cair aqui, a pessoa trabalha numa base
   isolada e ninguém vê o que ela digita, sem nenhum aviso na tela. É o que
   acontece com quem não tem o `Y:` mapeado.

Como três pessoas podem mexer juntas, antes de gravar o programa cria um
`dados.json.lock` e espera se outro PC estiver gravando. Isso protege a
**gravação**; não protege a **edição**: se dois abrirem a mesma ficha, quem
salvar por último vence.

### As duas planilhas da rede são necessárias

Não são "arquivos velhos". O botão **Restaurar da planilha** lê delas, e se o
`dados.json` se perder o painel se reconstrói a partir delas. Sem as duas, esse
caminho de recuperação deixa de existir.

---

## Os arquivos desta pasta

| Arquivo | Para que serve |
|---|---|
| `servidor.py` | o programa: servidor HTTP, leitura/gravação do `dados.json`, trava de rede, importação e exportação de Excel |
| `painel.html` | **a tela** — HTML, CSS e JavaScript. É aqui que se mexe no visual |
| `gerar_pagina.py` | converte o `painel.html` em `pagina.py` |
| `pagina.py` | **gerado automaticamente — não edite à mão** |
| `unificar_atendimentos.py` | leitura das planilhas de origem |
| `publicar.py` | faz tudo: gera a página, compila o .exe, empacota e publica |
| `_original\` | bytecode do .exe antigo, 73 KB, só como prova histórica |

---

## Como mexer e publicar

**Mudou alguma coisa? Um comando só:**

```
cd C:\Claude\painel-tercerizado
python publicar.py
```

Ele gera a página, compila o `.exe`, monta o `.rar`, guarda a versão anterior
em `_versao_anterior\` e publica no `Y:`. Avisa e para se o painel estiver
aberto (não dá para trocar um .exe em uso).

Para só gerar o `.exe` sem publicar nada:

```
python publicar.py --teste
```

**A armadilha:** se mexer no `painel.html` e compilar sem rodar o
`gerar_pagina.py` antes, o `.exe` sai com a tela velha e parece que a mudança
não funcionou. O `publicar.py` já faz isso por você — por isso use ele.

### Testar sem encostar na rede

```
set PAINEL_DADOS=C:\temp\teste-painel
python servidor.py
```

Copie um `dados.json` para essa pasta antes. Assim dá para importar, mover e
apagar séries à vontade sem risco para os dados de verdade.

---

## Modos de importação de Excel

| Modo | O que faz |
|---|---|
| **Sincronizar** (padrão) | a série é única: mesma série no mesmo estado + cidade + cliente não é tocada; em outro lugar, é **movida**; série que não veio no arquivo é **removida**; série inédita entra. Mostra relatório com de → para |
| Substituir | troca a lista inteira pela do arquivo |
| Merge | só acrescenta e atualiza, nunca remove |

No Sincronizar, **campo em branco na planilha não apaga** o que já está
preenchido no painel — o que foi digitado à mão sobrevive.

A comparação é por **UF + Cidade + Cliente**. Não existe campo de endereço: a
planilha tem a coluna `Endereço`, mas ela vem 100% vazia e o painel nunca a
guardou. Se um dia vier preenchida, dá para incluir na comparação.

---

## Regra da guia `--`

Equipamento em nome da **própria Solivetti** (qualquer cliente com "SOLIVETTI"
no nome) não fica na guia do estado: vai para a guia **`--`**, seja qual for a
UF que vier na planilha. Vale na importação, no cadastro manual e na edição.

As constantes estão no topo do `servidor.py` (`UF_PROPRIA`, `CLIENTE_PROPRIO`)
e a checagem é a função `_e_da_casa()`. Ela precisa ficar **antes** de
`construir_seed()` no arquivo, porque `DADOS = carregar_dados()` roda na hora
em que o módulo é importado.

O detalhe que faz a coisa funcionar: a regra é aplicada em `_ler_novos()`,
**antes** da comparação de movimento. Se fosse aplicada depois, cada
importação acharia que os equipamentos "voltaram" para PE e ficaria num
vai-e-vem eterno.

---

## Histórico

- **21/09/2026 (tarde)** — criada a regra da guia `--` (1.815 equipamentos
  migrados); removidos os botões "Baixar técnicos/equipamentos (CSV)", que
  exportavam colunas inexistentes (`cnpj`, `valorUnit`) e saíam vazias; a
  distribuição passou de `.zip` para `.rar`.
- **21/09/2026** — o `servidor.py` e o `unificar_atendimentos.py` tinham sido
  apagados da pasta `TERCERIZADO`; foram recuperados de dentro do próprio
  `painel.exe` (compilado com Python 3.14, a mesma versão da máquina, o que
  permitiu ler os code objects direto). A tela virou um `painel.html` de
  verdade em vez de uma string de 33 KB dentro do Python. Criado o modo
  **Sincronizar**.
- **03/08/2026** — pasta de dados mudou para o `Y:` (antes era `Z:`).
- **20/07/2026** — cada PC passou a rodar a própria instância em `localhost`,
  com os dados compartilhados na rede.

## Por que é um .exe e não um site

A TI não libera o firewall para entrada, não há Python instalado nos outros
PCs e os dados não podem ir para a internet. A pasta de rede ainda bloqueia
`.exe` e `.bat` por file-screening, mas aceita `.rar`, `.zip`, `.vbs` e
arquivos de dados. Por isso a distribuição é via **`.rar`**: a pessoa copia,
extrai e roda local. O `publicar.py` usa o `rar.exe` do WinRAR
(`C:\Program Files\WinRAR\`) e para com aviso se não achar.
