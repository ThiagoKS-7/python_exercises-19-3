jogo = [{
    'Pergunta': 'Quanto é 5x5?',
    'Opções': [100, 30, 25, 55],
    'Resposta': 25,
},
{
    'Pergunta': 'Qual o nome do meu cachorro?',
    'Opções': ['Soneca', 'Apollo', 'Bart', 'Henrique'],
    'Resposta': 'Apollo',
}]

for rodada in jogo:
    print(rodada['Pergunta'])
    for alternativas in rodada['Opções']:
        print(alternativas)
    resposta_final = input('R: ')

    if resposta_final == str(rodada['Resposta']):
        print('Resposta correta!')
    else:
        print('Resposta errada, tente novamente!')

