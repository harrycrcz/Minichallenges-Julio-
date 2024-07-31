class Figura:
    def __init__(self):
        pass

    def tipo_figura(self):
        print('Esta es una figura sin forma especifica')


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def tipo_figura(self):
        print(f'Esta figura es un circulo, y su radio es {self.radio}')


circulo = Circulo(8)
circulo.tipo_figura()
