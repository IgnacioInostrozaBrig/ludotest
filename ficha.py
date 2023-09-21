class Ficha:
    def __init__(self, player):
        self.player = player
        self.ingame = False  # Indica si la ficha está en juego o en la Partida
        self.coronada = False
        self.color = player.color
        self.final_track = False  # Indica si la ficha está en el camino final de su color
        self.winner = False  # Indica si la ficha ha ganado
        self.origin = player.origin
        self.position = self.origin
        self.valor = 1
        self.progress = 0

    def move(self, steps):
        # Actualiza el progreso de la ficha
        self.progress += steps
        if self.progress > 58:
            self.progress = 58

        # Verifica si la ficha ha completado una vuelta al tablero
        if self.progress > 52:
            self.final_track = True

        # Verifica si la ficha ha llegado al destino final
        if self.final_track and self.progress >= 58:
            self.winner = True
            print(f"Ficha del jugador {self.player.name} de color {self.color} ha llegado al destino final!")

        # Actualiza la posición de la ficha en juego
        self.position = (self.position + steps ) % 52
    
    def reset(self): #falta arreglarlo cuando está coronada
        self.ingame = False 
        self.coronada = False
        self.final_track = False  
        self.position = self.origin
        self.valor = 1
        self.progress = 0

