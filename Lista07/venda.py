import json

class Venda:
    def __init__(self, id, data, carrinho, total, idCliente):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.idCliente = idCliente
    
    def __str__(self) -> str:
        return f'{self.id}: {self.data} | {self.carrinho} | {self.total} | {self.idCliente}.'

class Vendas:
    objetos = []
    
    @classmethod
    def Abrir(cls):
        cls.objetos = []
        with open("vendas.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                v = Venda(obj["id"], obj["data"], obj["carrinho"], obj["total"], obj["idCliente"])
                cls.objetos.append(v)

    @classmethod
    def Salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
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
            x.data = obj.data
            x.carrinho = obj.carrinho
            x.total = obj.total
            x.idCliente = obj.idCliente
            cls.Salvar()