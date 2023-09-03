from dice import Dice
from board import Board
from player import Player
import random

class Game:
    def __init__(self):
        self.players = []
        self.current_player = None
        self.board = Board()
        self.dice = Dice()

    def initialize_players(self):
        self.players.clear()
        num_players = int(input("Ingrese la cantidad de jugadores (2-4): "))
        if num_players < 2 or num_players > 4:
            print("Número de jugadores no válido. Debe ser entre 2 y 4.")
            self.initialize_players()
            return
        for i in range(1, num_players + 1):
            name = input(f"Ingrese el nombre del jugador {i}: ")
            color = input(f"Ingrese el color del jugador {i}: ")
            self.players.append(Player(name, color))


    def start(self):
        self.initialize_players()

        # Determinar quién comienza lanzando el dado
        highest_roll = 0
        for player in self.players:
            input(f"Presiona Enter para que {player.name} tire el dado...")
            dice_value = self.dice.roll()
            print(f"{player.name} tiró un {dice_value}.")
            if dice_value > highest_roll:
                highest_roll = dice_value
                self.current_player = player

        print(f"{self.current_player.name} tiene el valor más alto y comienza el juego.")

        while True:
            input(f"Presiona Enter para que {self.current_player.name} juegue...")
            dice_value = self.dice.roll()
            print(f"{self.current_player.name} tiró un {dice_value}.")

            # Implementa la lógica para mover la ficha del jugador actual
            # Verifica las reglas del juego y actualiza el estado del juego

            # Cambia al siguiente jugador
            self.current_player = self.get_next_player()

    def get_next_player(self):
        # Implementa la lógica para determinar el próximo jugador
        pass

if __name__ == "__main__":
    game = Game()
    game.start()