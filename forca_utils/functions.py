def logout(kick):
    if (kick == "sair" or kick == "exit"):
        print("\nSaindo...\n")
        return True


def win(secret_word, rightLetters):
    if (secret_word.__len__() == rightLetters.__len__()):
        print(
            f"\nParabéns, você acertou, a palavra é '{secret_word.capitalize()}'\n")
        return True


def lose(chances, word):
    if (chances == 0):
        print(f"\nVocê foi enforcado, a palavra era {word}\n")
        return True


def kick():
    chute = str(input("Qual letra? "))
    return chute.strip() and chute.lower()


def chanceShow(chances, wrongLetters):
    
    if (chances < 7):
        print(f"Vocé ainda tem {chances} chances de acertar.\n")
        print(f"Letras erradas:\n{wrongLetters}\n")


def moreThanOneLetter(kick):
    if (kick.__len__() > 1):
        print("\nVocê deve digitar apenas uma letra.\n")
        return True
