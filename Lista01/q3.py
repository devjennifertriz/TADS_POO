class Banco:
    def __init__(self, titular, conta, saldo=0):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self, valor):
        print(f'O saldo atual da conta {self.conta} é de R${self.saldo}!')
        self.saldo += valor
        print(f'{self.titular} está depositando R${valor} na conta {self.conta}.')
        return print(f'O saldo atual da conta {self.conta} é de R${self.saldo}!')
    
    def sacar(self, valor):
        print(f'O saldo atual da conta {self.conta} é de R${self.saldo}!')
        self.saldo -= valor
        print(f'{self.titular} está sacando R${valor} da conta {self.conta}.')
        return print(f'O saldo atual da conta {self.conta} é de R${self.saldo}!')


pessoa = Banco('Jennifer', '45134-2', 100)
pessoa.depositar(200)
pessoa.sacar(50)
