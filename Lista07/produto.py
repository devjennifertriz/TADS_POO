import json

class Produto:
    def __init__(self, id:int, desc:str, preco:float, estoque:int, idCategoria:int):
        self.id = id
        self.desc = desc
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
    def __str__(self):
        return f'{self.id} - {self.desc} - {self.preco} - {self.estoque} - {self.idCategoria}'
    
class Produtos:
    objetos_produtos = []
    @classmethod
    def abrir(cls):
        cls.objetos_produtos = []
        with open("produto.json", mode='r') as arquivo:
            texto_prod = json.load(arquivo)
            for obj in texto_prod:
                prod = Produto(obj["id"], obj["desc"], obj["preco"], obj["estoque"], obj["idCategoria"])
                cls.objetos_produtos.append(prod)
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.objetos_produtos:
            if x.id == id: return x
        return None
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos_produtos
    def inserir(cls, id, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos_produtos:
            if x.id > id: id = x.id
        id += 1
        obj.id = id
        cls.objetos_produtos.append(obj)
        cls.salvar()
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            x.id = obj.id
            x.descricao = obj.descricao
            x.preco = obj.prec
            x.estoque = obj.estoque
            x.idCategoria = obj.idCategoria
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos_produtos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("produto.json", mode='w') as arquivo:
            json.dump(cls.objetos_produtos, arquivo, default= vars)
