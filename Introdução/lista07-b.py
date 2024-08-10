def Maior(a, b, c):
    maior = a #8
    if b > maior: #12 > #8
        maior = b
    elif c > maior:
        maior = c
    return print(f'{maior}')

x = int(input('Insira um número inteiro: '))
y = int(input('Insira um número inteiro: '))
z = int(input('Insira um número inteiro: '))

Maior(x, y, z)

    
    


