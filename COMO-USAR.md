# Como usar o Brandbook Sebrae 2026 com IA

Guia para quem quer aplicar o brandbook no dia a dia, sem precisar conhecer GitHub. Escolha a opção que combina com a ferramenta que você usa.

## Baixe os pacotes

| Pacote | Quando usar | Link |
| --- | --- | --- |
| Kit para IA | Projetos do Claude, ChatGPT, Gemini, Copilot ou qualquer ferramenta que aceite arquivos | [baixar](https://github.com/madsonp/brandbook-sebrae/releases/latest/download/brandbook-sebrae-kit-ia.zip) |
| Habilidade para o Claude | Quem usa o Claude e quer que a consulta ao brandbook aconteça automaticamente | [baixar](https://github.com/madsonp/brandbook-sebrae/releases/latest/download/brandbook-sebrae-habilidade-claude.zip) |

Os dois pacotes contêm apenas texto e dados (menos de 1 MB). Imagens das páginas e PDFs ficam no repositório, para baixar só quando necessário.

## Opção 1: habilidade do Claude (recomendada para quem usa Claude)

1. Baixe `brandbook-sebrae-habilidade-claude.zip`. Não descompacte.
2. No Claude, abra as configurações, procure a área de habilidades (Skills) e envie o arquivo .zip.
3. Ative a habilidade. A partir daí, sempre que você pedir algo sobre materiais do Sebrae, o Claude consulta o brandbook sozinho.

Se a sua conta não mostrar a área de habilidades, use a opção 2.

## Opção 2: projeto com o kit (qualquer ferramenta)

1. Baixe `brandbook-sebrae-kit-ia.zip` e descompacte.
2. Crie um projeto na sua ferramenta:
   - **Claude**: Projetos, novo projeto.
   - **ChatGPT**: Projetos ou um GPT personalizado.
   - **Gemini**: um Gem personalizado.
   - **Copilot**: um agente ou bloco de anotações com arquivos de referência.
3. Envie como conhecimento do projeto `GUIA-PARA-LLMS.md` e `brandbook-consolidado.md`. Envie também `CHECKLIST-DE-VALIDACAO.md` e `tokens/tokens-de-design.json`. Para valores detalhados de contraste e combinações, inclua os arquivos da pasta `dados/`.
4. Copie o conteúdo de `INSTRUCOES-PARA-O-ASSISTENTE.txt` para o campo de instruções do projeto.

Compartilhe o projeto com a equipe, se a ferramenta permitir, para que todos usem a mesma base.

## Opção 3: anexar só o necessário (uso pontual)

Para uma dúvida isolada, anexe na conversa o `brandbook-consolidado.md` e cole o texto de `INSTRUCOES-PARA-O-ASSISTENTE.txt` no início da mensagem.

## Quando a decisão depende de imagem

Logotipo, grid, proporções e exemplos visuais exigem a imagem da página. Localize a página no [índice](indice.md), baixe o arquivo correspondente em [`referencias-visuais/`](referencias-visuais/) ou o capítulo em [`pdfs-por-capitulo/`](pdfs-por-capitulo/) e anexe junto com o pedido. Um link no texto não faz a IA abrir a imagem.

## Para quem gera código (páginas, e-mails, apresentações em HTML)

Use as variáveis de [`tokens/tokens.css`](tokens/tokens.css) em vez de digitar códigos de cor. Exemplo de pedido: "Use as variáveis de tokens.css e confira a peça com o CHECKLIST-DE-VALIDACAO.md antes de entregar."

## Exemplos de pedidos

- "Revise este texto de post conforme o tom de voz do Sebrae e cite as páginas."
- "Quais cores posso usar para texto pequeno sobre fundo Atlântico no digital?"
- "Monte a hierarquia tipográfica de um cartaz A3 para evento do Sebraetec."
- "Esta submarca segue algum modelo de arquitetura do brandbook?"
- "Posso usar imagem gerada por IA neste material externo?"

## Limites

- É uma adaptação de consulta, não publicação oficial do Sebrae.
- Não inclui arquivos oficiais de logos, grids, ícones ou fontes. Solicite-os à área de comunicação.
- Algumas orientações são internas e provisórias, da Unidade de Portfólio e Marketing do Sebrae/BA, e aguardam resposta do Sebrae/NA. A IA deve identificá-las como tal.
- A IA pode errar. Confira as páginas citadas antes de aprovar uma peça.

Encontrou um erro ou tem sugestão? Veja [como contribuir](CONTRIBUINDO.md).
