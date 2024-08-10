print('=-' * 20)
nome = str(input('Digite o seu nome: '))
fix = float(input('Informe o seu Salário Fixo: '))
vendas = float(input('Informe o Total de Vendas efetuadas no mês: '))
porcent = (vendas * 15)/100
total = fix + porcent
print(f'O valor total recebido ao fim do mês é {total:.2f}')
