
import random

opcoes = ["pedra", "papel", "tesoura"]

computador = random.choice(opcoes)

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

print("Você escolheu:", jogador)
print("O computador escolheu:", computador)

if jogador not in opcoes:
    print("Opção inválida")

elif jogador == computador:
    print("Empate")

elif (jogador == "pedra" and computador == "tesoura" or
      jogador == "papel" and computador == "pedra" or
      jogador == "tesoura" and computador == "papel"):

    print("Você ganhou!")

else:
    print("Computador ganhou!")
