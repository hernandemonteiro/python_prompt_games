def logout(kick):
    if (kick == "sair" or kick == "exit"):
        print("\nSaindo...\n")
        return True


def win(secret_word, rightLetters):
    if (secret_word.__len__() == rightLetters.__len__()):
        print(
            f"\nParabéns, você acertou, a palavra é '{secret_word.capitalize()}'\n")
        return True


def lose(errors):
    if (errors == 7):
        print("\nVocê foi enforcado!\n")
        return True


def kick():
    chute = str(input("Qual letra? "))
    return chute.strip() and chute.lower()


def errorShow(errors, chances, wrongLetters):
    if (errors > 0):
        print(f"Vocé já errou {errors} vezes de {chances}.\n")
        print(f"Letras erradas:\n{wrongLetters}\n")
        return True


def moreThanOneLetter(kick):
    if (kick.__len__() > 1):
        print("\nVocê deve digitar apenas uma letra.\n")
        return True
