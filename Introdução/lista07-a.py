def Maior(a, b):
    if a > b:
        print(f'O valor {a} é maior que o valor {b}!')
    elif b > a:
        print(f'O valor {b} é maior que o valor {a}!')
    else:
        print(f'Ambos os valores {a} e {b} são iguais!')


x = int(input('Insira um número inteiro: '))
y = int(input('Insira um número inteiro: '))

Maior(x, y)
