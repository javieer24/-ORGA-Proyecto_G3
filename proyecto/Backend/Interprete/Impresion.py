class Impresion():
    def __init__(self, id, sentencias):
        self.id = id
        self.sentencias = sentencias
    
    def __str__(self) -> str:

        txt_sent = "; ".join(str(sent) for sent in self.sentencias)

        return f'{self.id}:\n{txt_sent}'

    def to_dict(self):
        return {
            "id": self.id,
            "sentencias": [sentencia.to_dict() for sentencia in self.sentencias]
        }


class Instruccion():

    def __init__(self, figura, color, fila, columna):
        self.figura = figura
        self.color = color
        self.fila = fila
        self.columna = columna
    
    def __str__(self) -> str:
        return f'{self.figura} {self.color} ({self.fila}, {self.columna}) '

    def to_dict(self):
        return {
            "figura": str(self.figura),
            "color": str(self.color),
            "fila": self.fila,
            "columna": self.columna
        }