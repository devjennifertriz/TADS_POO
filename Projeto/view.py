from cliente import Cliente, Clientes
from categoria import Categoria, Categorias
from produto import Produto, Produtos

class View:

    ## CLIENTES
    @staticmethod
    def clienteInserir(nome, email,  fone):
        cliente = Cliente(0, nome, email, fone)
        Clientes.Inserir(cliente)

    @staticmethod
    def clienteListar():
        return Clientes.Listar()
    
    @staticmethod
    def clienteAtualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        Clientes.Atualizar(cliente)

    @staticmethod
    def clienteExcluir(id):
        cliente = Cliente(id, '', '', '')
        Clientes.Excluir(cliente)

    ## CATEGORIA

    @staticmethod
    def categoriaInserir(desc):
        categoria = Categoria(desc)
        Categorias.Inserir(categoria)
    
    @staticmethod
    def categoriaListar():
        return Categorias.Listar()
    
    @staticmethod
    def categoriaAtualizar(desc):
        categoria = Categoria(desc)
        Categorias.Atualizar(categoria)

    @staticmethod
    def categoriaExcluir(id):
        categoria = Categoria(id, '', '', '')
        Categorias.Excluir(categoria)

    ##PRODUTO
    @staticmethod
    def produtoInserir(desc, preco, estoque, idCategoria):
        produto = Produto(desc, preco, estoque, idCategoria)
        Produtos.Inserir(produto)

    @staticmethod
    def produtoListar():
        return Produtos.Listar()
    
    @staticmethod
    def produtoAtualizar(id, desc, preco, estoque, idCategoria):
        produto = Produto(id, desc, preco, estoque, idCategoria)
        Produtos.Atualizar(produto)

    @staticmethod
    def produtoExcluir(id):
        produto = Produto(id, '', '', '')
        Produtos.Excluir(produto)
