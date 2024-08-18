from view import View

class UI:
    @staticmethod
    def Main():
        op = 0
        while op != 9:
            op = UI.Menu()
            if op == 1: UI.categoriaInserir()
            if op == 2: UI.categoriaListar()
            if op == 3: UI.categoriaAtualizar()
            if op == 4: UI.categoriaExcluir()

    @staticmethod
    def Menu():
        print('=== Seja bem-vindo(a) ao Comércio Eletrônico! ===')
        print('             Menu de Operações')
        print('1: Inserir | 2: Listar | 3: Atualizar | 4: Excluir | 9: Sair')
        return int(input('Insira uma opção: '))
    
    @staticmethod
    def categoriaInserir():
        desc = input('Insira a descrição para a categoria: ')
        View.categoriaInserir(desc)

    @staticmethod
    def categoriaListar():
        for cliente in View.categoriaListar():
            print(cliente) 

    @staticmethod
    def categoriaAtualizar():
        UI.categoriaListar
        id = int(input('Informe o #ID da categoria que será atualizada: '))
        desc = input('Insira a descrição para a categoria: ')
        View.categoriaAtualizar(id, desc)

    @staticmethod
    def categoriaExcluir():
        UI.categoriaListar()
        id = int(input('Informe o #ID do cliente que será removido: '))
        View.categoriaExcluir(id)
  
UI.Main()