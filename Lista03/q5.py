class Data():
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def setDia(self, d):
        if d < 32: self.__dia = d

    def setMes(self, m):
        if m <= 12: self.__mes = m
    
    def setAno(self, a):
        self.__ano = a

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano

    def SetData(self):
        return f'{self.__dia}/{self.__mes}/{self.__ano}'

    def __str__(self):
        return f'{self.__dia}/{self.__mes}/{self.__ano}'

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.nova_data()
        
    @staticmethod
    def menu():
        print('1 - Nova data, 2 - Fim')
        return int(input("Informe uma opção: "))

    @staticmethod
    def nova_data():
        d = int(input("Insira um dia do ano: "))
        m = int(input("Insira um mês do ano: "))
        a = int(input("Insira um ano da década: "))
        d = Data(d, m, a)
        print(f'A data de hoje é {d}.')

UI.main()