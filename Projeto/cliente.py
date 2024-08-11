import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f'{self.id}: {self.nome} | {self.email} | {self.fone}.'
    
class Clientes:
    objetos = []
    @classmethod
    def Abrir(cls):
        cls.objetos = []
        with open("clientes.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.objetos.append(c)
    
    @classmethod
    def Salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
        id += 1
        obj.id = id
        cls.objetos.append(obj)
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.objetos
    
    @classmethod
    def Listar_ID(cls, id):
        cls.Abrir()
        for x in cls.objetos:
            if x.id == id: return x
        return None
    
    @classmethod
    def Excluir(cls, obj):
        x = cls.Listar_ID(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.Salvar()

    @classmethod
    def Atualizar(cls, obj):
        x = cls.Listar_ID(obj.id)
        if x != None:
            x.nome = obj.nome
            x.email = obj.email
            x.fone = obj.fone
            cls.Salvar()

    
        