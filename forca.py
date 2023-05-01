from random import randrange
from forca.forca_utils import *


def play():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    fruits = ["banana", "maça", "uva", "pera", "morango",
              "abacaxi", "goiaba", "melancia", "laranja"]
    secret_word = fruits[randrange(0, fruits.__len__())]
    secret_word_array = list(secret_word.__len__() * "-")

    play = bool(True)
    rightLetters = []

    wrongLetters = []
    errors = 0
    chances = 7

    while (play):
        if win(secret_word, rightLetters):
            break
        if lose(errors):
            break

        print(f"\nPalavra Secreta:\n{secret_word_array}\n")

        errorShow(errors, chances, wrongLetters)

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
            errors += 1




if (__name__ == '__main__'):
    play()
