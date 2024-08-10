def Aprovado(n1, n2):
    média = (n1 + n2)/2
    print(f'A média final foi de... {média}.')
    if média >= 60:
        print('O aluno está Aprovado!')
    if 30 <= média < 60:
        print('O aluno está em Prova Final!')
    else:
        print('O aluno está Reprovado!')

nota1 = int(input('Insira a primeira nota do bimestre: '))
nota2 = int(input('Insira a segunda nota do bimestre: '))

Aprovado(nota1, nota2)