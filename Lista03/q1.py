import math

class Retangulo():
    def __init__(self, b, h):
        self.__b = b
        self.__h = h

    def setBase(self, b):
        if self.__b > 0: self.__b = b
        else: return ValueError()

    def setAltura(self, h):
        if self.__h > 0: self.__h = h
        else: return ValueError()
    
    def GetBase(self):
        return self.__b
    
    def GetAltura(self):
        return self.__h
    
    def CalcArea(self):
        a = self.__b * self.__h
        return a

    def CalcDiagonal(self):
        #d = d ** 2 + self.__b ** 2 + self.__h ** 2
        d = math.sqrt(self.__b ** 2 + self.__h ** 2)
        return d

    def __str__(self):
        return f'A base do retângulo é {self.__b} e sua altura é {self.__h}.'  
    

r = Retangulo(8, 6)