import json

class Produto:
    def __init__(self, id, desc, preco, estoque, idCategoria):
        self.id = id
        self.desc = desc
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria

    def __str__(self) -> str:
        return f'{self.id}: | {self.desc} | {self.preco} | {self.estoque} | {self.idCategoria}.'

class Produtos:
    objetos = []
    
    @classmethod
    def Abrir(cls):
        cls.objetos = []
        with open("produto.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                p = Produto(obj["id"], obj["desc"], obj["preco"], obj["estoque"], obj["idCategoria"])
                cls.objetos.append(p)

    @classmethod
    def Salvar(cls):
        with open("produto.json", mode="w") as arquivo:
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
            x.desc = obj.desc
            x.preco = obj.preco
            x.estoque = obj.estoque
            x.idCategoria = obj.idCategoria
            cls.Salvar()
        