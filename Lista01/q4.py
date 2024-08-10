class Cinema:
    def __init__(self, dia_semana):
        self.dia_semana = dia_semana
        self.valor_ingresso = 0

    def calcular_ingresso(self):
        if self.dia_semana in ['Segunda', 'segunda', 'Terça,', 'Quinta', 'quinta']:
            self.valor_ingresso = 16.0
        elif self.dia_semana in ['Quarta', 'quarta']:
            self.valor_ingresso = 8.0
        else:
            self.valor_ingresso = 20.0

        return print(f'{self.valor_ingresso}')
    
p1 = Cinema('quarta')
p1.calcular_ingresso()
    
