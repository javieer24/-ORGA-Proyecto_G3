from enum import Enum

class FIGURA(Enum):
    VACIO = 1
    EQUIS = 2
    CIRCULO = 3
    TRIANGULO = 4
    ESTRELLA = 5


    def __str__(self):
        return str(self.name)

class COLOR(Enum):
    BLANCO = 1
    CYAN = 2
    MAGENTA = 3
    YELLOW = 4
    BLACK = 5

    def __str__(self):
        return str(self.name)