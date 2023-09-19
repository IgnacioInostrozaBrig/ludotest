class Ficha:
    def __init__(self, player):
        self.player = player
        self.position = -1  # -1 indica que la ficha está en la Partida
        self.coronada = False
        self.color = player.color
        self.final_track = False
        self.valor = 1

    def move(self, steps):
        # Implementa la lógica para mover la ficha según los pasos dados
        pass