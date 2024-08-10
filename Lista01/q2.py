class Viagem:
    def __init__(self):
        self.dist = 0
        self.tempo = 0

    def calc_media(self):
        return self.dist / self.tempo

x = Viagem()
x.dist = float(input('Insira a distância percorrida: '))
x.tempo = float(input('Insira o tempo gasto na viagem: '))
print(f'A velocidade média foi de {x.calc_media()} km/h')