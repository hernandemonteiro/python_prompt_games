from random import randrange
from forca_utils.functions import chanceShow, kick, moreThanOneLetter, logout, win, lose


def play():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')
    print('*** Para sair digite "sair" ou "exit" ***')

    fruits = ["banana", "maça", "uva", "pera", "morango",
              "abacaxi", "goiaba", "melancia", "laranja"]
    secret_word = fruits[randrange(0, len(fruits))]
    secret_word_array = list(len(secret_word) * "-")

    play = bool(True)
    rightLetters = []

    wrongLetters = []
    chances = 7

    points = 0

    while (play):
        if lose(chances, secret_word):
            break
        print(f"\nPalavra Secreta:\n{secret_word_array}\n")
        if win(secret_word, rightLetters):
            points += 1
            print(f"Você tem {points} pontos\n")
            rightLetters = []
            wrongLetters = []
            chances = 7
            secret_word = fruits[randrange(0, len(fruits))]
            secret_word_array = list(len(secret_word) * "-")
            continue

        chanceShow(chances, wrongLetters)

        chute = kick()

        if logout(chute):
            break

        if moreThanOneLetter(chute):
            continue

        index = 0
        for letra in secret_word:
            if (chute == letra):
                secret_word_array[index] = letra
                rightLetters.append(letra)
            index += 1
        if (chute not in secret_word and chute not in wrongLetters):
            wrongLetters.append(chute)
            chances -= 1


if (__name__ == '__main__'):
    play()
