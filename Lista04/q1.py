from random import randint

class Bingo():
    def __init__(self) -> None:
        self.__numBolas = []
        self.__bolas = []

        self.__numBolas(randint)

    def Proximo(self):
        return self.__numBolas(randint, self.__numBolas)
    
    def Sorteados(self, bolas):
        pass

    def __str__(self):
        return f'{self.__numBolas}'

b = Bingo()

    