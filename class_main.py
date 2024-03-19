import string
from typing import Any
class Rodada:
    def __init__(self, obj:dict) -> None:
        self.pontos = 0
        self.pergunta = obj["pergunta"]
        self.opcoes = obj["opcoes"]
        self.chute = None
        self.resposta = obj["resposta"]
        self.alternativas = string.ascii_lowercase[:len(self.opcoes)] if len(self.opcoes) > 0 else []
    def jogar(self):
        while str(self.chute) not in str(rodada.resposta):
            indice = 0
            print(self.pergunta)
            while indice < len(self.opcoes):
                print(self.alternativas[indice] + ") " + str(self.opcoes[indice]))
                indice += 1
            self.chute = input("R: ")
            if str(self.chute) in str(rodada.resposta):
                self.pontos += 1
                print(f"Resposta correta!")
            else:
                print(f"Resposta errada, tente novamente!")
        return self.pontos

jogo =[
    Rodada({"pergunta": "Quanto é 5 x 5?", "opcoes": [100, 30, 25, 55], "resposta":["c",25]}),
    Rodada({"pergunta":"Qual o nome do meu cachorro?", "opcoes": ["Soneca", "Apollo", "Bart", "Henrique"],
            "resposta": ["b","Apollo"]})
]
pontos = 0
for rodada in jogo:
    pontos += rodada.jogar()
    print(f"Pontos {pontos}")
