from random import randrange
from adivinhacao.InputUserNumber import InputUserNumber

game = InputUserNumber()
secret_number = randrange(0, 10)

print("\n*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************\n")

print("De 0 a 10 tente adivinhar o numero secreto que estou pensando...\n")


i = 0
while (i < 7):
    game.ask()

    if (secret_number == game.kick):
        print("\nParabéns você acertou!\n")
        break
    else:
        print("\nTente novamente!\n")
        i += 1
    print(f"Você tem {7 - i} tentativas!\n")
