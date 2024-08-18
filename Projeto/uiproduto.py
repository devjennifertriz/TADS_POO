from view import View

class UI:
    @staticmethod
    def Main():
        op = 0
        while op != 9:
            op = UI.Menu()
            if op == 1: UI.produtoInserir()
            if op == 2: UI.produtoListar()
            if op == 3: UI.produtoAtualizar()
            if op == 4: UI.produtoExcluir()

    @staticmethod
    def Menu():
        print('=== Seja bem-vindo(a) ao Comércio Eletrônico! ===')
        print('             Menu de Operações')
        print('1: Inserir | 2: Listar | 3: Atualizar | 4: Excluir | 9: Sair')
        return int(input('Insira uma opção: '))
    
    @staticmethod
    def produtoInserir():
        nome = input('Informe o nome do cliente: ')
        email = input('Informa o e-mail do cliente: ')
        fone = input('Informe o número de contato do cliente: ')
        View.produtoInserir(nome, email, fone)

    @staticmethod
    def produtoListar():
        for cliente in View.clienteListar():
            print(cliente) 

    @staticmethod
    def produtoAtualizar():
        UI.produtoListar()
        id = int(input('Informe o #ID do produto que será atualizado: '))
        desc = input('Insira uma descrição para o produto: ')
        preco = input('Insira o preço da categoria: ')
        estoque = input('Insira a quantidade de produtos em estoque: ')
        categoria = input('Insira a categoria do produto: ')
        View.produtoAtualizar(id, desc, preco, estoque, categoria)

    @staticmethod
    def produtoExcluir():
        UI.produtoListar()
        id = int(input('Informe o #ID do cliente que será removido: '))
        View.produtoExcluir(id)
  
UI.Main()