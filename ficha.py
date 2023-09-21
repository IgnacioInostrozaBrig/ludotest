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
        if not self.ingame and steps not in [1, 6]:
            print("La ficha no puede moverse si no está en juego y no se sacó un 1 o un 6.")
            return

        # Calcula la nueva posición de la ficha
        new_position = self.origin + self.progress + steps

        # Verifica si la ficha ha completado una vuelta al tablero
        if new_position >= 52:
            self.final_track = True
            new_position -= 52

        # Actualiza el progreso de la ficha
        self.progress += steps

        # Verifica si la ficha ha llegado al destino final
        if self.final_track and self.progress >= 52:
            self.winner = True

            print(f"Ficha del jugador {self.player.name} de color {self.color} ha llegado al destino final!")

        # Actualiza la posición de la ficha en juego
        self.position = (self.position + steps ) % 52
        self.ingame = True
    
    def reset(self): #falta arreglarlo cuando está coronada
        self.ingame = False 
        self.coronada = False
        self.final_track = False  
        self.position = self.origin
        self.valor = 1
        self.progress = 0

