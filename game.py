import tkinter as tk
from dice import Dice
from board import Board
from player import Player
from interface import Interface


class Game:
    def __init__(self, root):
        self.players = []
        self.current_player = None
        self.board = Board(root)
        self.dice = Dice()
        self.board.create()

    def initialize_players(self):
        self.players.clear()
        num_players = int(input("Ingrese la cantidad de jugadores (2-4): "))
        if num_players < 2 or num_players > 4:
            print("\033[91mNúmero de jugadores no válido. Debe ser entre 2 y 4.\033[00m")
            self.initialize_players()
            return

        playerCount = 0
        for i in range(1, num_players + 1):
            name = input(f"Ingrese el nombre del jugador {i}: \n")
            if name == "":
                name = f"Jugador {playerCount + 1}"
            if playerCount == 0:
                color = "\033[34mazul\033[00m"
                origin = 0
            elif playerCount == 1:
                color = "\033[31mrojo\033[00m"
                origin = 13
            elif playerCount == 2:
                color = "\033[32mverde\033[00m"
                origin = 26
            else:
                color = "\033[33mamarillo\033[00m"
                origin = 39
            self.players.append(Player(name, color, origin))
            print(f"{name} ha sido inscrito con el color {color}\n")
            playerCount += 1

    def start(self):
        Interface.start()
        self.initialize_players()

        # Determinar quién comienza lanzando el dado
        highest_roll = 0
        players_with_highest_roll = []

        for player in self.players:
            input(f"Presiona Enter para que {player.name} de color {player.color} tire el dado...\n")
            dice_value = self.dice.roll()
            print(f"{player.name} tiró un {dice_value}.")

            if dice_value > highest_roll:
                highest_roll = dice_value
                players_with_highest_roll = [player]
            elif dice_value == highest_roll:
                players_with_highest_roll.append(player)

        if len(players_with_highest_roll) > 1:
            # Si hay empate, realiza un desempate lanzando el dado entre los jugadores empatados
            print("Hubo un empate!\n")
            while len(players_with_highest_roll) > 1:
                highest_roll = 0
                new_players_with_highest_roll = []

                for player in players_with_highest_roll:
                    input(f"Presiona Enter para que {player.name} de color {player.color} tire el dado...\n")
                    dice_value = self.dice.roll()
                    print(f"{player.name} tiró un {dice_value}.")

                    if dice_value > highest_roll:
                        highest_roll = dice_value
                        new_players_with_highest_roll = [player]
                    elif dice_value == highest_roll:
                        new_players_with_highest_roll.append(player)

                players_with_highest_roll = new_players_with_highest_roll

        self.current_player = players_with_highest_roll[0]
        print(f"{self.current_player.name} tiene el valor más alto y comienza el juego.\n")

        while True:
            print(self.current_player.name + "\n")
            input(f"Presiona Enter para que {self.current_player.name} de color {self.current_player.color} juegue...\n")
            dice_value = self.dice.roll()
            print(f"{self.current_player.name} tiró un {dice_value}.\n")

            # Implementa la lógica para mover la ficha del jugador actual
            if dice_value == 1 or dice_value == 6:
                if self.current_player.ingresar_ficha()==True:
                    print(f"{self.current_player.name} ha agregado una ficha al tablero.\n")
                    for ficha in self.current_player.fichas:
                        if ficha.ingame == False:
                            ficha.ingame = True
                            ficha.move(0)
                            break
                else:
                    print(f"{self.current_player.name} se ha movido {dice_value} posiciones .\n")
                    self.current_player.ultima_ficha().move(dice_value)
                
            else:
                if self.current_player.ultima_ficha() == False:
                    print(f"{self.current_player.name}, necesita un 1 o un 6 para ingresar una ficha.\n")
                else:
                    print(f"{self.current_player.name} se ha movido {dice_value} posiciones .\n")
                    self.current_player.ultima_ficha().move(dice_value)



            # ver si cae en ficha de otro jugador
            for ficha in self.current_player.fichas:
                if ficha.ingame == True:
                    for player in self.players:
                        for ficha_enemiga in player.fichas:
                            if ficha.position == ficha_enemiga.position and ficha_enemiga.final_track == False:
                                ficha_enemiga.reset()

            #ver cuando se corona


            if self.current_player.ganador() == True:
                print(f"{self.current_player.name} es el ganador.\n")
                break

            # Cambia al siguiente jugador
            self.current_player = self.get_next_player(dice_value)
            print("\n")
            print("\n")

    def get_next_player(self, dice_value):
        if dice_value == 1 or dice_value == 6:
            return self.current_player
        else:
            for player in self.players:
                if player == self.current_player:
                    current_index = self.players.index(player)
                    break
            return self.players[(current_index + 1) % len(self.players)]

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x640")
    root.maxsize(1000,640)
    root.minsize(1000,640)
    root.title('Ludo')

    game = Game(root)
    game.start()

    root.mainloop()





