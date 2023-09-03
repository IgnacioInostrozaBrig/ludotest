from ficha import Ficha

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.fichas = [Ficha(self) for _ in range(4)]
        self.finished_fichas = 0