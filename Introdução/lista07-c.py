def Iniciais(nome):
    name = nome.split(' ')
    for i in name:
        print(f'{i[0]}', end=' ')

nome = str(input('Informe o seu nome completo: '))

Iniciais(nome)
