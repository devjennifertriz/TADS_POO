import json

class VendaItem:
    def __init__(self, id:int, qtd:int, preco:float, idVenda:int, idProduto:int):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.idVenda = idVenda
        self.idProduto = idProduto
    def __str__(self):
        return f"{self.id} - {self.qtd} - {self.preco} - {self.idVenda} - {self.idProduto}"
        
class VendaItems:
    objetos_venda = []
    @classmethod
    def abrir(cls):
        cls.objetos_venda = []
        with open("vendaitem.json", mode ='r') as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                venda = VendaItem(obj["id"], obj["qtd"], obj["preco"], obj["idVenda"], obj["idProduto"])
                cls.objetos_venda.append(venda)
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.objetos_venda:
            if x.id == id: return x
        return None
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos_venda
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos_venda:
            if x.id > id: id = x.id
        id +=1
        obj.id = id
        cls.objetos_venda(obj)
        cls.salvar()
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            x.qtd = obj.qtd
            x.preco = obj.preco
            x.idVenda = obj.idVenda
            x.idProduto = x.idProduto
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos_venda.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("vendaitem.json", mode='w') as arquivo:
            json.dump(cls.objetos_venda, arquivo, default= vars)

        