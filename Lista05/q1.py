from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

        if self.__nome == "": raise ValueError()
        if nascimento > datetime.now() : raise ValueError("Data de nascimento não pode ser no futuro")

    def setNome(self, nome):
        self.__nome = nome

    def setCPF(self, cpf):
        self.__cpf = cpf
    
    def setTelefone(self, telefone):
        self.__telefone = telefone

    def setNascimento(self, nascimento):
        self.__nascimento = nascimento

    def getNome(self):
        return self.__nome
    
    def getCPF(self):
        return self.__cpf
    
    def getTelefone(self):
        return self.__telefone
    
    def getNascimento(self):
        return self.__nascimento
    
    def Idade(self):
        today = datetime.now()
        idade = today - self.__nascimento
        anos = idade.days // 365
        return f'O paciente tem {anos} anos.'
    
    def __str__(self):
        return f"Paciente: {self.__nome} -- CPF: {self.__cpf} -- Telefone: {self.__telefone} -- Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}"

class UI:
    def main():
        nascimento = input('Insira a Data de Nascimento: ')
        data = datetime.strptime(nascimento, '%d/%m/%Y')
        nome = input('Insira o nome do paciente: ')
        cpf = input('Insira o seu CPF: ')
        telefone = input('Insira o seu telefone: ')
        pessoa = Paciente(nome, cpf, telefone, data)
        print(pessoa)
        print(pessoa.Idade())

UI.main()


