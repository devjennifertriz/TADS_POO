class Musica():
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

        if self.__artista == "": return ValueError()
        if self.__album == "": return ValueError()

    def setTitulo(self, titulo):
        if self.__titulo != "": self.__titulo = titulo
        else: return ValueError()
    def setArtista(self, artista):
        if self.__artista != "": self.__artista = artista
        else: return ValueError()
    def setAlbum(self, album):
        if self.__album != "": self.__album = album
        else: return ValueError()
    def getTitulo(self):
        return self.__titulo
    def getArtista(self):
        return self.__artista
    def getAlbum(self):
        return self.__album
    
    def __str__(self) -> str:
        return f'{self.__titulo} --> {self.__artista}, {self.__album}'
    
class Playlist():
    def __init__(self, nome):
        self.__nome = nome
        self.__musicas = []

    def getNome(self, nome):
        if self.__nome != "": self.__nome = nome
        else: return ValueError()

    def setNome(self):
        return self.__nome
    
    def Inserir(self, musica):
        self.__musicas.append(musica)

    def Listar(self, musica):
        for musica in self.__musicas:
            print(musica)

    def __str__(self) -> str:
        return f'{self.__nome} possui {len(self.__musicas)}'


m = Musica('Wonderwall', 'Oasis', 'What is the glory?')
playlist = Playlist('Rock')
playlist.Inserir(m)