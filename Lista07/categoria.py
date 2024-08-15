import json

class Categoria:
    def __init__(self, id, desc):
        self.id = id
        self.desc = desc

    def __str__(self) -> str:
        return f'{self.id}: {self.desc}.'

class Categorias:
    objetos = []
    
    @classmethod
    def Abrir(cls):
        cls.objetos = []
        with open("categorias.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                cat = Categoria(obj["id"], obj["desc"])
                cls.objetos.append(cat)

    @classmethod
    def Salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
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
            cls.Salvar()