from ficha import Ficha

class Player:
    def __init__(self, name, color, origin):
        self.name = name
        self.color = color
        self.origin = origin
        self.fichas = [Ficha(self) for _ in range(4)]
        self.finished_fichas = 0