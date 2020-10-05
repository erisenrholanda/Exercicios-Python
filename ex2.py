# 2. Elabore um programa para solicitar o nome de uma equipe de futebol, a quantidade de derrotas, empates e
# vitórias obtidas por ela no campeonato. No futebol, cada vitória vale três pontos e cada empate vale um ponto.
# Calcular e informar: a quantidade de pontos ganhos, a quantidade de pontos perdidos e o percentual de aproveitamento
# da equipe.

time = input('informe o nome do time: ')
vitorias = int(input('quantas vitorias: '))
derrotas = int(input('quantas derrotas: '))
empates = int(input('quantas empates: '))

pontosTotais = vitorias * 3 + empates
totalDeJogos = vitorias+derrotas+empates
pontosPerdidos = derrotas*3+empates*2
aproveitamento = pontosTotais / (totalDeJogos * 3) * 100

print('O time do {} jogou um total de {}'.format(time, totalDeJogos), 'jogos')
print('tendo um total de:', vitorias, 'vitorias')
print('tendo um total de:', derrotas, 'derrotas')
print('tendo um total de:', empates, 'empates')
print('total de pontos perdidos', pontosPerdidos)
print('tendo um total de {} pontos'.format(pontosTotais))
print('aproveitamento do time foi: {:.2f}$'.format(aproveitamento))
