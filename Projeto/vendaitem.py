import json

class Item:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.idVenda = idVenda
        self.idProduto = idProduto
    
    def __str__(self) -> str:
        return f'{self.id}: {self.qtd} | {self.preco} | {self.idVenda} | {self.idProduto}'

class VendaItem:
    objetos = []
    
    @classmethod
    def Abrir(cls):
        cls.objetos = []
        with open("vendaitem.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                i = Item(obj["id"], obj["qtd"], obj["preco"], obj["idVenda"], obj["idProduto"])
                cls.objetos.append(i)

    @classmethod
    def Salvar(cls):
        with open("vendaitem.json", mode="w") as arquivo:
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
            x.qtd = obj.qtd
            x.preco = obj.preco
            x.idVenda = obj.idVenda
            x.idProduto = obj.idProduto
            cls.Salvar()