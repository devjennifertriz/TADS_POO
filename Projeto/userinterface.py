from view import View

class UI:
    @staticmethod
    def Main():
        op = 0
        while op != 9:
            op = UI.MenuPrincipal()
            if op == 1: UI.clienteInserir()
            if op == 2: UI.clienteListar()
            if op == 3: UI.clienteAtualizar()
            if op == 4: UI.clienteExcluir()

    @staticmethod
    def MenuPrincipal():
        print('=== Seja bem-vindo(a) ao Comércio Eletrônico! ===')
        print('             Menu de Operações')
        print('1: Inserir | 2: Listar | 3: Atualizar | 4: Excluir | 9: Sair')
        return int(input('Insira uma opção: '))
    
    @staticmethod
    def clienteInserir():
        nome = input('Informe o nome do cliente: ')
        email = input('Informa o e-mail do cliente: ')
        fone = input('Informe o número de contato do cliente: ')
        View.clienteInserir(nome, email, fone)

    @staticmethod
    def clienteListar():
        for cliente in View.clienteListar():
            print(cliente)

    @staticmethod
    def clienteAtualizar():
        UI.clienteListar()
        id = int(input('Informe o #ID do cliente que será atualizado: '))
        nome = input('Informe o nome do cliente: ')
        email = input('Informa o e-mail do cliente: ')
        fone = input('Informe o número de contato do cliente: ')
        View.clienteAtualizar(id, nome, email, fone)

    @staticmethod
    def clienteExcluir():
        UI.clienteListar()
        id = int(input('Informe o #ID do cliente que será removido: '))
        View.clienteExcluir(id)
  
UI.Main()

    

