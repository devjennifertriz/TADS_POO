class Disciplina():
    def __init__(self, nome, semestre, media, ch):
        self.__nome = nome
        self.__semestre = semestre
        self.__media = media
        self.__ch = ch
        self.__aprovado = self.__media >= 60

    def setNome(self, nome):
        self.__nome = nome    

    def setSemestre(self, semestre):
        self.__semestre = semestre    

    def setMedia(self, media):
        if self.__media > 0 and self.__media < 100: self.__media = media 
        else: return ValueError()

    def setCargaH(self, ch): 
        self.__ch = ch 
    def getNome(self):
        return self.__nome
    def getSemestre(self):
        return self.__semestre
    def getMedia(self):
        return self.__media
    def getCargaH(self):
        return self.__ch

    def __str__(self):
        return f'A disciplina {self.__nome} foi cursada no semestre {self.__semestre}, com média de {self.__media} e foi {self.__aprovado}'
    
d = Disciplina('Matemática', 2024, 75, 100)
print(d)

