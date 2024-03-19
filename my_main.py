import string
jogo = [
    ("Quanto é 5 x 5?", [100, 30, 25, 55], ["c", 25]),
    ("Qual o nome do meu cachorro?", ["Soneca", "Apollo", "Bart", "Henrique"], ["b", "Apollo"])
]
pontos = 0
rodadas = 0
chute = None


for rodada in jogo:
    alternativas = string.ascii_lowercase[:len(rodada[1])]
    while str(chute) !=  str(rodada[2][0]) and (str(chute) != str(rodada[2][1])):
        print(rodada[0])
        for opt in range(len(rodada[1])):
            print(alternativas[opt] + ") " + str(rodada[1][opt]) )
        chute =input("R: ")
        if (str(chute) == str(rodada[2][0])) or (str(chute) == str(rodada[2][1])):
            pontos += 1
            print(f"Resposta correta!\nPontos: {pontos}")
        else:
            print(f"Resposta errada, tente novamente!\nPontos: {pontos}")
