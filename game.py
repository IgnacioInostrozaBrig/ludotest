from dice import Dice
from board import Board
from player import Player
from interface import Interface
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
            print("\033[91mNúmero de jugadores no válido. Debe ser entre 2 y 4.\033[00m")
            self.initialize_players()
            return
        
        playerCount = 0
        for i in range(1, num_players + 1):
            name = input(f"Ingrese el nombre del jugador {i}: ")
            if (playerCount == 0):
                color = "\033[34mazul\033[00m"
            elif (playerCount == 1):
                color = "\033[31mrojo\033[00m"
            elif (playerCount == 2):
                color = "\033[32mverde\033[00m"
            else:
                color = "\033[33mamarillo\033[00m"
            self.players.append(Player(name, color))
            print(name + " ha sido inscrito con el color "+ color)
            playerCount += 1


    def start(self):
        Interface.start()
        self.initialize_players()

        # Determinar quién comienza lanzando el dado
        highest_roll = 0
        for player in self.players:
            input(f"Presiona Enter para que {player.name} de color {player.color} tire el dado...")
            dice_value = self.dice.roll()
            print(f"{player.name} tiró un {dice_value}.")
            if dice_value > highest_roll:
                highest_roll = dice_value
                self.current_player = player

        print(f"{self.current_player.name} tiene el valor más alto y comienza el juego.")

        while True:
            print(self.current_player.name)
            input(f"Presiona Enter para que {self.current_player.name} de color {self.current_player.color} juegue...")
            dice_value = self.dice.roll()
            print(f"{self.current_player.name} tiró un {dice_value}.")

            # Implementa la lógica para mover la ficha del jugador actual
            # Verifica las reglas del juego y actualiza el estado del juego

            # Cambia al siguiente jugador
            self.current_player = self.get_next_player()

    def get_next_player(self):
        for player in self.players:
            if player == self.current_player:
                current_index = self.players.index(player)
                break
        return self.players[(current_index + 1) % len(self.players)]

if __name__ == "__main__":
    game = Game()
    game.start()