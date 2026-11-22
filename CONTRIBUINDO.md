# Como contribuir

## Relatar erro ou sugerir melhoria

Abra uma ocorrência na aba [Issues](https://github.com/madsonp/brandbook-sebrae/issues/new/choose) e escolha o modelo:

- **Divergência com o brandbook**: o material diz algo diferente do PDF original, ou a IA respondeu errado usando este material.
- **Sugestão**: novo conteúdo, exemplo de pedido ou melhoria no kit.

Informe sempre a página do PDF envolvida.

## Alterar arquivos

1. Crie um ramo e proponha a alteração por solicitação de mesclagem (pull request).
2. Preserve `original.pdf` e `referencias-visuais/`.
3. Mantenha coerentes o consolidado, os capítulos em `regras/` e os dados em `dados/`.
4. Se alterar arquivo coberto por `dados/inventario-sha256.json`, atualize o inventário.
5. Execute `python scripts/verificar.py` e `python scripts/gerar-pacotes.py`.

A verificação roda automaticamente em cada proposta.

## Publicar nova versão dos pacotes

Crie uma marcação de versão (por exemplo `v5.1.1`) no ramo principal. A automação verifica o repositório, gera os dois pacotes e publica na seção [Releases](https://github.com/madsonp/brandbook-sebrae/releases). Os links de download do `COMO-USAR.md` passam a apontar para a versão nova.
