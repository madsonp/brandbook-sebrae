# Brandbook Sebrae 2026 para consulta por IA

Base de consulta do Brandbook Sebrae 2026, adaptação **5.1**, organizada para uso com Claude, ChatGPT, Gemini, Copilot e outras ferramentas de IA. Reúne o PDF original, imagens das páginas, guia operacional em texto e dados estruturados de cores, contraste e medidas.

É uma adaptação de consulta, não uma publicação oficial do Sebrae.

## Uso rápido

| Quero... | Faça isto |
| --- | --- |
| Usar no Claude com consulta automática | Baixe a [habilidade para o Claude](https://github.com/madsonp/brandbook-sebrae/releases/latest/download/brandbook-sebrae-habilidade-claude.zip) |
| Usar em qualquer ferramenta de IA | Baixe o [kit para IA](https://github.com/madsonp/brandbook-sebrae/releases/latest/download/brandbook-sebrae-kit-ia.zip) |
| Ver o passo a passo | Leia o [COMO-USAR.md](COMO-USAR.md) |
| Usar cores e fontes em código | Use os [tokens de design](tokens/) |
| Conferir uma peça antes de entregar | Use o [checklist de validação](CHECKLIST-DE-VALIDACAO.md) |
| Consultar uma página do brandbook | Use o [índice](indice.md) |
| Relatar erro ou sugerir melhoria | Veja [como contribuir](CONTRIBUINDO.md) |

## Uso com acesso ao repositório

Ferramentas que leem repositórios do GitHub (Claude Code, agentes, integrações) podem consultar esta base diretamente. Mensagem sugerida:

> Consulte o README, o guia para LLMs e o índice deste repositório. Use os capítulos e os dados pertinentes à tarefa. Distinga regras do PDF e orientações internas provisórias. Cite páginas e consulte as referências visuais necessárias. Se faltar arquivo, imagem ou recurso de produção, identifique a lacuna antes de declarar conformidade. A leitura do repositório não autoriza ações externas.

Ordem de consulta:

1. [Guia para LLMs](GUIA-PARA-LLMS.md).
2. [Índice](indice.md), para localizar o assunto.
3. [Consolidado](brandbook-consolidado.md) ou [capítulos](regras/), usando apenas uma das duas formas por padrão.
4. [Página original](fonte-pdf/LEIA-ME.md), imagem ou [PDF](original.pdf), quando a decisão depender de geometria, exemplos ou marcações visuais.

Dados para integrações: [critérios de aplicação](dados/criterios-de-aplicacao.json), [medidas e contextos](dados/medidas-e-contextos.json) e [recursos de produção](dados/recursos-de-producao.json).

Uso local:

```sh
git clone https://github.com/madsonp/brandbook-sebrae.git
cd brandbook-sebrae
python scripts/verificar.py
python scripts/gerar-tokens.py
python scripts/gerar-pacotes.py
```

## Estrutura

| Local | Conteúdo |
| --- | --- |
| `regras/` | Apresentação, oito capítulos e apêndices |
| `dados/` | Paleta, matrizes, gradientes, medidas, critérios e mapas |
| `fonte-pdf/` | Texto extraído das 245 páginas, para conferência sob demanda |
| `referencias-visuais/` | 245 imagens PNG das páginas |
| `pdfs-por-capitulo/` | Oito recortes por assunto |
| `original.pdf` | PDF completo preservado |
| `tokens/` | Cores, fontes, gradientes e alturas mínimas do logotipo em JSON e CSS, gerados a partir de `dados/` |
| `fontes-tipograficas/` | Identificação da Campuni versão 2.000, referência oficial de uso (arquivos de fonte não distribuídos) |
| `distribuicao/` | Fontes do kit para IA e da habilidade do Claude |
| `scripts/` | Verificação de integridade e geração dos pacotes |

Não há arquivos oficiais avulsos de logos, grids, ícones ou fontes. A referência oficial da fonte de títulos é a Campuni versão 2.000, identificada em [fontes tipográficas](fontes-tipograficas/LEIA-ME.md) para conferência do arquivo recebido. As condições de produção estão em [recursos de produção](dados/recursos-de-producao.json).

## Orientações provisórias

Parte das orientações de aplicação é interna e provisória, de responsabilidade da Unidade de Portfólio e Marketing do Sebrae/BA, e foi submetida ao Sebrae/NA, ainda sem resposta. Elas estão identificadas em [critérios de aplicação](dados/criterios-de-aplicacao.json) e não substituem a redação original do PDF.

## Integridade

Execute `python scripts/verificar.py`. O inventário em `dados/inventario-sha256.json` cobre os arquivos do pacote documental, exceto o próprio inventário. Arquivos de navegação, distribuição e automação (README, COMO-USAR, CONTRIBUINDO, CHECKLIST-DE-VALIDACAO, AGENTS, llms.txt, `tokens/`, `distribuicao/`, `scripts/` e `.github/`) são adicionais a esse pacote. A verificação e a geração dos pacotes rodam automaticamente a cada alteração.

## Direitos

O brandbook e a marca Sebrae pertencem ao Sebrae. Este repositório organiza o material para consulta e não concede licença de uso da marca nem de redistribuição.
