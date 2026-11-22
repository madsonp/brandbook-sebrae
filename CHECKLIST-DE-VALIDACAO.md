# Checklist de validação

Antes de entregar qualquer material com a marca Sebrae, responda sim ou não a cada item que se aplica à peça. Um "não" ou "não verificado" deve ser informado na entrega. Não declare conformidade com o brandbook se algum item aplicável ficou sem verificação.

## Cores

1. [ ] Todos os códigos de cor estão em `tokens/tokens-de-design.json` (pp. 67 e 68), sem códigos derivados ou aproximados?
2. [ ] Cada par de texto e fundo aparece como aprovado em `dados/contraste-texto-fundo.json`, para o meio (digital ou impresso) e a categoria de tamanho (grande ou pequena) corretos (pp. 89 a 92)?
3. [ ] Para composição gráfica, a combinação aparece sem restrição em `dados/combinacoes-graficas.json` para a cor-base e o meio corretos (pp. 69 a 75)?
4. [ ] Se houver gradiente: é peça digital, com duas cores, 50% de cada, 45°, usando um par mostrado nas pp. 77 ou 79 (p. 76)?

## Tipografia

5. [ ] Títulos e subtítulos em Campuni Bold versão 2.000, conferida pelo SHA-256 de `fontes-tipograficas/LEIA-ME.md` (p. 82), e textos em Figtree (p. 83)? Se alguma fonte foi substituída, isso foi informado?
6. [ ] A hierarquia segue a escala título 1x, subtítulo x/2, texto x/4, com espaço entre estilos não menor que a altura do texto seguinte (p. 84)?
7. [ ] Entreletra, se usada, foi convertida em em, nunca em px (pp. 85 e 86)?

## Logotipo e assinatura

8. [ ] O logotipo veio de arquivo oficial, sem recriação com texto digitado ou redesenho?
9. [ ] Nenhum uso indevido: cor alterada (salvo versões oficiais preta e branca da p. 201), distorção, rotação, elemento eliminado ou modificado (p. 222)?
10. [ ] A área de proteção, com X igual à altura da letra S, está livre de outros elementos (p. 202)?
11. [ ] A altura respeita o mínimo da configuração usada: 10 mm ou 50 px no logotipo isolado; 12 mm ou 65 px na composta com descritivo à direita; 18 mm ou 96 px nas compostas com descritivo abaixo (p. 203)?
12. [ ] A configuração da assinatura (isolada, composta, com parceiros ou selos) corresponde à finalidade da peça (pp. 198 a 221)?

## Imagem e grid

13. [ ] Fotografias sem intervenções gráficas, efeitos, iluminação forçada, poses forçadas ou ângulos que desfavoreçam a pessoa empreendedora, e sem preto e branco nas fotografias institucionais (p. 104)?
14. [ ] O grid foi aplicado a partir de modelo oficial, sem cortar módulos pela metade nem alterar escalas (pp. 105 a 121)?
15. [ ] Ícones, se houver, são oficiais ou construídos no grid 10x12, com uso pontual e não protagonista (pp. 125 a 127)?

## Linguagem

16. [ ] O texto é próximo, positivo e específico, sem colocar o Sebrae como protagonista da jornada do cliente (p. 33)?
17. [ ] No máximo um ponto de exclamação seguido (p. 33)?
18. [ ] Linguagem inclusiva aplicada, sem "homem" como genérico e sem masculino para pessoas indeterminadas (p. 52)?

## Inteligência artificial e origem das regras

19. [ ] Se houve conteúdo gerado por IA, as condições das pp. 226 a 231 foram conferidas, inclusive a validação para uso externo?
20. [ ] Toda orientação provisória de `dados/criterios-de-aplicacao.json` usada na peça foi identificada como tal, e não como regra do PDF?
21. [ ] Faltou algum arquivo oficial (logotipo, grid, fonte, ícone)? Se sim, a entrega foi identificada como rascunho e o recurso ausente foi nomeado?
