"""Gera os pacotes de distribuição em dist/.

- brandbook-sebrae-kit-ia.zip: kit em texto para projetos de Claude, ChatGPT, Gemini e similares.
- brandbook-sebrae-habilidade-claude.zip: habilidade (Skill) para enviar ao Claude.

Uso: python scripts/gerar-pacotes.py
"""
from pathlib import Path
import json
import zipfile

raiz = Path(__file__).resolve().parents[1]
dist = raiz / 'dist'
DATA_FIXA = (2026, 1, 1, 0, 0, 0)

DADOS = [
    'cores.csv',
    'cores-contextuais.json',
    'contraste-texto-fundo.csv',
    'contraste-texto-fundo.json',
    'combinacoes-graficas.csv',
    'gradientes.json',
    'intervalos-gradientes.json',
    'medidas-e-contextos.json',
    'criterios-de-aplicacao.json',
    'recursos-de-producao.json',
    'links-extraidos-do-pdf.json',
    'mapa-paginas.csv',
    'manifesto.json',
]


def escrever(zf, origem: Path, destino: str):
    info = zipfile.ZipInfo(destino, DATA_FIXA)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    zf.writestr(info, origem.read_bytes())


def gerar(nome, pasta, itens):
    caminho = dist / nome
    with zipfile.ZipFile(caminho, 'w') as zf:
        for origem, destino in itens:
            escrever(zf, origem, f'{pasta}/{destino}')
    return caminho


def main():
    dist.mkdir(exist_ok=True)
    edicao = json.loads((raiz / 'dados/manifesto.json').read_text(encoding='utf-8'))['edicao_adaptacao']
    dados = [(raiz / 'dados' / n, f'dados/{n}') for n in DADOS]

    kit = [
        (raiz / 'distribuicao/kit/LEIA-PRIMEIRO.md', 'LEIA-PRIMEIRO.md'),
        (raiz / 'distribuicao/kit/INSTRUCOES-PARA-O-ASSISTENTE.txt', 'INSTRUCOES-PARA-O-ASSISTENTE.txt'),
        (raiz / 'GUIA-PARA-LLMS.md', 'GUIA-PARA-LLMS.md'),
        (raiz / 'brandbook-consolidado.md', 'brandbook-consolidado.md'),
        (raiz / 'CHECKLIST-DE-VALIDACAO.md', 'CHECKLIST-DE-VALIDACAO.md'),
        (raiz / 'tokens/tokens-de-design.json', 'tokens/tokens-de-design.json'),
        (raiz / 'tokens/tokens.css', 'tokens/tokens.css'),
    ] + dados

    habilidade = [
        (raiz / 'distribuicao/habilidade-claude/SKILL.md', 'SKILL.md'),
        (raiz / 'GUIA-PARA-LLMS.md', 'referencias/GUIA-PARA-LLMS.md'),
        (raiz / 'CHECKLIST-DE-VALIDACAO.md', 'referencias/CHECKLIST-DE-VALIDACAO.md'),
        (raiz / 'tokens/tokens-de-design.json', 'referencias/tokens/tokens-de-design.json'),
        (raiz / 'tokens/tokens.css', 'referencias/tokens/tokens.css'),
    ] + [(p, f'referencias/regras/{p.name}') for p in sorted((raiz / 'regras').glob('*.md'))] \
      + [(o, f'referencias/{d}') for o, d in dados]

    gerados = [
        gerar('brandbook-sebrae-kit-ia.zip', 'brandbook-sebrae-kit', kit),
        gerar('brandbook-sebrae-habilidade-claude.zip', 'brandbook-sebrae', habilidade),
    ]
    print(json.dumps({
        'edicao': edicao,
        'pacotes': {p.name: f'{p.stat().st_size / 1024:.0f} KB' for p in gerados},
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
