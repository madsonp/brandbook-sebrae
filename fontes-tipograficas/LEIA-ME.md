# Fontes tipográficas: referência oficial de uso

Este diretório identifica as fontes de produção da marca. Os arquivos de fonte não são distribuídos neste repositório público. Não substitui a leitura das páginas 81 a 86 nem de [dados/fontes-tipograficas.json](../dados/fontes-tipograficas.json).

## Campuni, versão 2.000

A versão 2.000 da Campuni é a referência oficial de uso para produção. Obtenha os arquivos pelos canais internos de comunicação do Sebrae e confira se correspondem à identificação abaixo.

| Arquivo esperado | Peso | Uso no PDF | Tamanho | SHA-256 |
| --- | --- | --- | --- | --- |
| `Campuni-Bold.otf` | Bold | Peso prescrito para títulos e subtítulos (p. 82) | 77.204 bytes | `b8773cca2d43ab78db4478a85165ae364077a8c9f788e08973054afc8f742820` |
| `Campuni-Regular.otf` | Regular | Não é o peso dos títulos. O PDF a embute só na p. 120 | 76.164 bytes | `efb70161878ff8c05ec622f24cd4b933173c3e20e15b7dc7b8deab7c530d6a9a` |
| `Campuni-Black.otf` | Black | Não ocorre no PDF e não está prescrita para a marca-mãe | 74.456 bytes | `1872920b6fa1c1f5d5c3c7ece8e0090693f0c55af1c06f10f59eec9c3e7b4c83` |

Para conferir um arquivo recebido:

```sh
sha256sum Campuni-Bold.otf        # Linux
shasum -a 256 Campuni-Bold.otf    # macOS
certutil -hashfile Campuni-Bold.otf SHA256   # Windows
```

Se o resultado for diferente, o arquivo não é a versão de referência.

O copyright é de Moritz Kleinsorge (2020). A tabela OS/2 declara `fsType` 8 (incorporação editável). Este repositório não distribui os arquivos nem cria licença de redistribuição.

O `original.pdf` incorpora um recorte anterior, de 2018, em grade de 2048. A versão 2.000 usa grade de 1000 e revisa contornos. Para produzir, usar a versão 2.000. Para descrever o desenho de uma página, consultar o PDF.

## Demais famílias

- **Figtree** (textos, p. 83): disponível no [Google Fonts](https://fonts.google.com/specimen/Figtree). O arquivo não foi baixado e a licença não foi verificada nesta base.
- **Univers** (nomes de submarcas, pp. 156 e 160): arquivos não incluídos.

Corpo, entrelinha e entreletra medidos nas pp. 82 a 86 e 93 estão em [dados/fontes-tipograficas.json](../dados/fontes-tipograficas.json).
