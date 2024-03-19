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


letters = ['A', 'B', 'C', 'D']

for rodada in jogo:


    options_with_letters = zip(letters, rodada['Opções']) # cria um array de tuplas (letra, opcao)
    sorted_options = sorted(options_with_letters, key=lambda x: x[0]) # organiza pra garantir que  "A" seja a primeira
    rodada['Opções'] = [f"{letter}: {option}" for letter, option in sorted_options] #lista de strings formatada das opt

    print(rodada['Pergunta'])
    for alternativas in rodada['Opções']:
        print(alternativas)

    resposta_input = input('R:')

    if resposta_input.upper() in letters:
        resposta_final = [option for letter, option in sorted_options if letter == resposta_input.upper()][0]
    else:
        resposta_final = str(resposta_input)


    if resposta_final == rodada['Resposta']:
        print('Resposta correta!')
    else:
        print('Resposta errada, tente novamente!')