"""Gera tokens/tokens-de-design.json e tokens/tokens.css a partir de dados/.

Os tokens são derivados exclusivamente dos dados extraídos do PDF. Não edite os
arquivos de tokens à mão: altere os dados e execute novamente este script.

Uso: python scripts/gerar-tokens.py
"""
from pathlib import Path
import csv
import json
import unicodedata

raiz = Path(__file__).resolve().parents[1]
saida = raiz / 'tokens'


def chave(nome):
    sem_acento = unicodedata.normalize('NFKD', nome).encode('ascii', 'ignore').decode()
    return sem_acento.lower().replace(' ', '-')


def carregar(nome):
    return json.loads((raiz / 'dados' / nome).read_text(encoding='utf-8'))


def main():
    saida.mkdir(exist_ok=True)
    manifesto = carregar('manifesto.json')

    cores = {}
    with open(raiz / 'dados/cores.csv', encoding='utf-8-sig') as f:
        for linha in csv.DictReader(f):
            cores[chave(linha['nome'])] = {
                'nome': linha['nome'],
                'grupo': linha['grupo'],
                'hex': linha['hex'],
                'rgb': [int(v) for v in linha['rgb'].split(',')],
                'cmyk': [int(v) for v in linha['cmyk'].split(',')],
                'pantone': linha['pantone'],
                'pagina_pdf': int(linha['pagina_pdf']),
            }
    for c in carregar('cores-contextuais.json'):
        cores[chave(c['nome'])] = {
            'nome': c['nome'],
            'grupo': c['grupo'],
            'hex': c['hex'],
            'rgb': c['rgb'],
            'cmyk': None,
            'pantone': None,
            'paginas_pdf': c['paginas_pdf'],
            'observacao': c['origem_codigo'],
        }

    gradientes = carregar('gradientes.json')
    campuni = carregar('fontes-tipograficas.json')
    bold = next(a for a in campuni['arquivos'] if a['peso'] == 'Bold')
    tokens = {
        'titulo': 'Tokens de design do Brandbook Sebrae 2026',
        'edicao_adaptacao': manifesto['edicao_adaptacao'],
        'origem': 'Gerado por scripts/gerar-tokens.py a partir de dados/. Não editar à mão.',
        'limites': [
            'Use somente os códigos desta tabela; não derive novos códigos das cores exibidas no PDF (pp. 67 e 68).',
            'Combinação de cores não mostrada no PDF não significa combinação aprovada. Para texto sobre fundo, consulte dados/contraste-texto-fundo.json; para composição gráfica, dados/combinacoes-graficas.json.',
            'Os tokens não substituem os arquivos oficiais de logotipo, grid, ícones e fontes, que não estão no repositório.',
        ],
        'cores': cores,
        'tipografia': {
            'familias': {
                'titulos': {'familia': 'Campuni', 'peso': 'Bold', 'versao_de_referencia': campuni['versao'],
                            'arquivo_esperado': bold['arquivo'].split('/')[-1], 'sha256': bold['sha256'],
                            'distribuicao': 'Arquivo não distribuído no repositório; ver fontes-tipograficas/LEIA-ME.md.',
                            'paginas_pdf': [82]},
                'texto': {'familia': 'Figtree', 'pesos': ['Regular', 'Bold'], 'paginas_pdf': [83],
                          'download': 'https://fonts.google.com/specimen/Figtree'},
                'nomes_de_submarcas': {'familia': 'Univers', 'observacao': 'Pesos conforme o modelo de arquitetura; ver regras/05-arquitetura-de-marcas.md.', 'paginas_pdf': [156, 160]},
            },
            'fonte_alternativa': 'Não definida no PDF. Se a fonte oficial não estiver disponível, declare a substituição e trate a peça como rascunho.',
            'hierarquia': {
                'escala': [
                    {'estilo': 'titulo', 'familia': 'Campuni Bold', 'tamanho': '1x'},
                    {'estilo': 'subtitulo', 'familia': 'Campuni Bold', 'tamanho': 'x/2'},
                    {'estilo': 'texto_destaque', 'familia': 'Figtree Bold', 'tamanho': 'x/4'},
                    {'estilo': 'texto', 'familia': 'Figtree Regular', 'tamanho': 'x/4'},
                ],
                'espaco_entre_estilos': 'Nunca menor que a altura do texto que vem a seguir.',
                'pagina_pdf': 84,
            },
            'entreletra': 'Valores em milésimos de em (convenção provável, pendente do Sebrae/NA): -10 equivale a letter-spacing: -0.01em; nunca em px. Ver pp. 85 e 86.',
        },
        'gradientes': {
            'regra': {'meio': 'digital', 'cores': 2, 'proporcao': '50% de cada cor', 'angulo_graus': 45, 'pagina_pdf': 76},
            'pares_mostrados': [{'grupo': g['grupo'], 'cores': [g['cor_1'], g['cor_2']], 'pagina_pdf': g['pagina_pdf']} for g in gradientes],
            'cores_para_texto_e_grafismos_sobre_gradiente': {
                i['grupo_gradiente']: {'cores': i['cores_solidas_no_intervalo'], 'pagina_pdf': i['pagina_pdf']}
                for i in carregar('intervalos-gradientes.json')
            },
            'limite': 'A ordem dos nomes identifica o par mostrado; não define coordenadas ou paradas de gradiente.',
        },
        'logotipo': {
            'area_de_protecao': 'Altura da letra S (X) em todos os lados do retângulo que tangencia o logotipo (p. 202).',
            'usos_indevidos': ['Não mudar a cor do logotipo, salvo as versões oficiais preta e branca (p. 201).',
                               'Não distorcer as proporções.', 'Não rotacionar.',
                               'Não eliminar nenhum elemento.', 'Não modificar nenhum elemento.'],
            'pagina_usos_indevidos': 222,
            'altura_minima': {
                'pagina_pdf': 203,
                'observacao': 'Valores em mm e px são limites distintos do original; não converter entre si. Endossos sem barras: p. 166.',
                'configuracoes': [
                    {'assinatura': 'Logotipo isolado, com barras', 'impresso_mm': 10, 'digital_px': 50},
                    {'assinatura': 'Composta versão 3 (descritivo à direita), p. 199', 'impresso_mm': 12, 'digital_px': 65},
                    {'assinatura': 'Composta versão 1 (descritivo centralizado abaixo), p. 199', 'impresso_mm': 18, 'digital_px': 96},
                    {'assinatura': 'Composta versão 2 (descritivo abaixo, à esquerda), p. 199', 'impresso_mm': 18, 'digital_px': 96},
                ],
            },
        },
    }
    (saida / 'tokens-de-design.json').write_text(
        json.dumps(tokens, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    linhas = [
        '/* Tokens de design do Brandbook Sebrae 2026, adaptação '
        f"{manifesto['edicao_adaptacao']}.",
        '   Gerado por scripts/gerar-tokens.py a partir de dados/. Não editar à mão.',
        '   Códigos das pp. 67 e 68. Para pares de texto e fundo, consulte dados/contraste-texto-fundo.json. */',
        ':root {',
    ]
    for k, c in cores.items():
        linhas.append(f"  --sebrae-{k}: {c['hex']}; /* {c['nome']}, {c['grupo']} */")
    linhas += [
        '',
        "  --sebrae-fonte-titulo: 'Campuni', sans-serif; /* Bold, versão 2.000 de referência, p. 82 */",
        "  --sebrae-fonte-texto: 'Figtree', sans-serif; /* Regular e Bold, p. 83 */",
        '  /* Escala da p. 84: título 1x, subtítulo x/2, texto x/4. Defina x conforme a peça. */',
        '}',
        '',
    ]
    (saida / 'tokens.css').write_text('\n'.join(linhas), encoding='utf-8')
    print(json.dumps({'cores': len(cores), 'pares_de_gradiente': len(gradientes)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
