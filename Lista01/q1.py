class Circulo:
    def __init__(self):
        self.raio = 0
        
    def calc_area(self):
        return (self.raio ** 2) * 3.14

x = Circulo()
x.raio = int(input('Insira o raio: '))
print(x.calc_area())