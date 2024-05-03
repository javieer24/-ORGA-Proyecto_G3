class Figura:
    def __init__(self, forma, color, vacio):
        self.forma = forma
        self.color = color
        self.vacio = vacio
    
    def binario(self):
        if self.forma == 'estrella':
            if self.color == 'cyan':
                return '00001b'
            if self.color == 'magenta':
                return '00011b'
            if self.color == 'yellow':
                return '00101b'
            if self.color == 'black':
                return '00111b'
        if self.forma == "equis":
            if self.color == 'cyan':
                return '01001b'
            if self.color == 'magenta':
                return '01011b'
            if self.color == 'yellow':
                return '01101b'
            if self.color == 'black':
                return '01111b'
        if self.forma == "circulo":
            if self.color == 'cyan':
                return '10001b'
            if self.color == 'magenta':
                return '10011b'
            if self.color == 'yellow':
                return '10101b'
            if self.color == 'black':
                return '10111b'
        if self.forma == "triangulo":
            if self.color == 'cyan':
                return '11001b'
            if self.color == 'magenta':
                return '11011b'
            if self.color == 'yellow':
                return '11101b'
            if self.color == 'black':
                return '11111b'
            
        if self.vacio:
            return '00000b'
        