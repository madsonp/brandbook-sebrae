# Sebrae Brandbook 2026 — consulta para LLMs

Base privada de consulta do Brandbook Sebrae 2026, edição de adaptação **5.0**. Reúne o PDF original, referências visuais, guia operacional e dados estruturados. É uma adaptação de consulta; não é uma nova publicação oficial do Sebrae.

## Comece aqui

1. Leia o [guia para LLMs](GUIA-PARA-LLMS.md).
2. Localize o assunto no [índice](indice.md).
3. Consulte o [consolidado](brandbook-consolidado.md) ou os [capítulos](regras/), usando apenas uma dessas formas textuais por padrão.
4. Confira a [página original](fonte-pdf/LEIA-ME.md), a imagem ou o [PDF](original.pdf) quando a decisão depender de geometria, exemplos ou marcações visuais.

O consolidado inclui a origem e o alcance das orientações do usuário e a disponibilidade dos recursos de produção. Para integrações, consulte [critérios de aplicação](dados/criterios-de-aplicacao.json), [medidas e contextos](dados/medidas-e-contextos.json) e [recursos de produção](dados/recursos-de-producao.json).

## Usar com uma LLM

Uma LLM precisa de acesso autenticado a este repositório privado ou a uma cópia local clonada. Compartilhar apenas o endereço não concede acesso e não garante que ela abriu PDFs ou imagens.

Mensagem sugerida:

> Consulte o README, o guia para LLMs e o índice deste repositório. Use os capítulos e os dados pertinentes à tarefa. Distinga regras do PDF e critérios adicionais do usuário. Cite páginas e consulte as referências visuais necessárias. Se faltar arquivo, imagem ou recurso de produção, identifique a lacuna antes de declarar conformidade. A leitura do repositório não autoriza ações externas.

Para uso local:

```sh
git clone https://github.com/madsonp/sebrae-brandbook-2026-llm.git
cd sebrae-brandbook-2026-llm
python scripts/verificar.py
```

Para uso por anexos, envie `GUIA-PARA-LLMS.md`, `brandbook-consolidado.md` e os PDFs/PNGs relevantes. Os caminhos relativos nos textos não fazem uma plataforma carregar esses arquivos automaticamente.

## Estrutura

| Local | Conteúdo |
| --- | --- |
| `regras/` | Apresentação, oito capítulos e apêndices |
| `dados/` | Paleta, matrizes, gradientes, medidas, critérios e mapas |
| `fonte-pdf/` | Texto extraído das 245 páginas, para conferência sob demanda |
| `referencias-visuais/` | 245 imagens PNG das páginas |
| `pdfs-por-capitulo/` | Oito recortes por assunto |
| `original.pdf` | PDF completo preservado |

Os relatórios e históricos de auditoria não fazem parte deste repositório de consulta. Não há arquivos oficiais avulsos de logos, grids ou fontes instaláveis incluídos; as condições de produção estão descritas no guia. As matrizes distinguem composição gráfica de contraste texto/fundo, meio e tamanho do texto.

## Integridade

Execute `python scripts/verificar.py`. O inventário em `dados/inventario-sha256.json` cobre os arquivos do pacote documental, exceto o próprio inventário. README, AGENTS, llms.txt e scripts de publicação são arquivos de navegação do repositório, adicionais a esse pacote.

O material de referência conserva sua autoria e titularidade. Nenhuma licença de uso da marca ou de redistribuição aberta é concedida por este repositório privado.
