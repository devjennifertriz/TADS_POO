from cliente import Cliente, Clientes
from produto import Produto, Produtos
from categoria import Categoria, Categorias

class UI:
    @staticmethod
    def Main(op):
        while op != 9:
            if op == 1: UI.MenuCliente()
            if op == 2: UI.MenuProduto()
            if op == 3: UI.MenuCategoria()

    @staticmethod
    def MenuPrincipal():
        print('=== Seja bem-vindo(a) ao Comércio Eletrônico! ===')
        print('           Menu de Operações')
        print('1: Cliente | 2: Produto | 3: Categoria | 0: Sair')
        op = int(input("Insira uma opção: "))
        UI.Main(op)
    
    ## @MENUCLIENTE
    @staticmethod
    def MainCliente(op):
        while op != 0:
            if op == 1: UI.clienteInserir()
            if op == 2: UI.clienteListar()
            if op == 3: UI.clienteAtualizar()
            if op == 4: UI.clienteExcluir()
            else: UI.MenuPrincipal()
        
    @staticmethod
    def MenuCliente():
        print(' ====== Menu CLIENTE ===== ')
        print('1: Inserir | 2: Listar | 3: Atualizar | 4: Excluir | 0: Sair')
        op = int(input('Insira uma opção: '))
        UI.MainCliente(op)
    
    @staticmethod
    def clienteInserir():
        nome = input('Informe o nome do cliente: ')
        email = input('Informa o e-mail do cliente: ')
        fone = input('Informe o número de contato do cliente: ')
        cliente = Cliente(0, nome, email, fone)
        Clientes.Inserir(cliente)
        UI.MenuCliente()

    @staticmethod
    def clienteListar():
        for clientes in Clientes.Listar():
            print(clientes)

    @staticmethod
    def clienteAtualizar():
        UI.clienteListar()
        id = int(input('Informe o #ID do cliente que será atualizado: '))
        nome = input('Informe o nome do cliente: ')
        email = input('Informa o e-mail do cliente: ')
        fone = input('Informe o número de contato do cliente: ')
        cliente = Cliente(id, nome, email, fone)
        Clientes.Atualizar(cliente)
        UI.MenuCliente()

    @staticmethod
    def clienteExcluir():
        UI.clienteListar()
        id = int(input('Informe o #ID do cliente que será removido: '))
        cliente = Cliente(id, '', '', '')
        Clientes.Excluir(cliente)
        UI.MenuCliente()

    ## @MENUPRODUTO
    @staticmethod
    def MainProduto(op):
        while op != 0:
            if op == 1: UI.produtoInserir()
            if op == 2: UI.produtoListar()
            if op == 3: UI.produtoAtualizar()
            if op == 4: UI.produtoExcluir()
            else: UI.MenuPrincipal()

    @staticmethod
    def MenuProduto():
        print(' ====== Menu PRODUTO ===== ')
        print('1: Inserir | 2: Listar | 3: Atualizar | 4: Excluir | 0: Sair')
        op = int(input('Insira uma opção: '))
        UI.MainProduto(op)

    @staticmethod
    def produtoInserir():
        desc = input('Insira uma descrição para o produto: ')
        preco = input('Insira o preço do produto: ')
        estoque = input('Insira a quantidade de produtos em estoque: ')
        categoria = input('Insira a categoria do produto: ')
        produto = Produto(0, desc, preco, estoque, categoria)
        Produtos.Inserir(produto)
        UI.MenuProduto()

    @staticmethod
    def produtoListar():
        for produto in Produtos.Listar():
            print(produto)

    @staticmethod
    def produtoAtualizar():
        UI.produtoListar()
        id = int(input('Informe o #ID do produto que será atualizado: '))
        desc = input('Insira uma descrição para o produto: ')
        preco = input('Insira o preço da categoria: ')
        estoque = input('Insira a quantidade de produtos em estoque: ')
        categoria = input('Insira a categoria do produto: ')
        produto = Produto(id, desc, preco, estoque, categoria)
        Produtos.Atualizar(produto)
        UI.MenuProduto()

    @staticmethod
    def produtoExcluir():
        UI.produtoListar()
        id = int(input('Informe o #ID do produto que será removido: '))
        produto = Produto(id, '', '', '', '')
        Produtos.Excluir(produto)
        UI.MenuProduto()

    ## @MENUCATEGORIA
    @staticmethod
    def MainCategoria(op):
        while op != 0:
            if op == 1: UI.categoriaInserir()
            if op == 2: UI.categoriaListar()
            if op == 3: UI.categoriaAtualizar()
            if op == 4: UI.categoriaExcluir()
            else: UI.MenuPrincipal()
    
    @staticmethod
    def MenuCategoria():
        print(' ====== Menu CATEGORIA ===== ')
        print('1: Inserir | 2: Listar | 3: Atualizar | 4: Excluir | 0: Sair')
        op = int(input('Insira uma opção: '))
        UI.MainCategoria(op)

    @staticmethod
    def categoriaInserir():
        desc = input('Insira a descrição para a categoria: ')
        categoria = Categoria(0, desc)
        Categorias.Inserir(categoria)
        UI.MenuCategoria()

    @staticmethod
    def categoriaListar():
        for categoria in Categorias.Listar():
            print(categoria)

    @staticmethod
    def categoriaAtualizar():
        UI.categoriaListar()
        id = int(input('Informe o #ID da categoria que será atualizada: '))
        desc = input('Insira a descrição para a categoria: ')
        categoria = Categoria(id, desc)
        Categorias.Atualizar(categoria)
        UI.MenuCategoria()

    @staticmethod
    def categoriaExcluir():
        UI.categoriaListar()
        id = int(input('Informe o #ID da categoria que será removida: '))
        categoria = Categoria(id, '')
        Categorias.Excluir(categoria)
        UI.MenuCategoria()
    
UI.MenuPrincipal()

    

