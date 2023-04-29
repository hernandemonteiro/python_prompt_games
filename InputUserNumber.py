class InputUserNumber:
    kick = 0

    @classmethod
    def ask(number):
        number_inputed = int(input("Digite seu numero: "))
        InputUserNumber.kick = number_inputed

