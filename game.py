import tkinter as tk
from tkinter import *
from tkinter import ttk
from dice import Dice
from board import Board, BoardColor
from player import Player
from interface import Interface


class Game:
    def __init__(self, root):
        self.players = []
        self.current_player = None
        self.board = Board(root, self)
        self.dice = Dice()
        self.board.create()
        self.playerbase = 0

    def initialize_players(self, player_num):
        self.players.clear()
        num_players = int(player_num)
        if num_players < 2 or num_players > 4:
            print("\033[91mNúmero de jugadores no válido. Debe ser entre 2 y 4.\033[00m")
            self.initialize_players()
            return

        playerCount = 0
        for i in range(1, num_players + 1):
            name = ""
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
        
        self.start()

    def start(self):
        Interface.start()
        #self.initialize_players()

        # Determinar quién comienza lanzando el dado
        highest_roll = 0
        players_with_highest_roll = []

        for player in self.players:
            #input(f"Presiona Enter para que {player.name} de color {player.color} tire el dado...\n")
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
                    #input(f"Presiona Enter para que {player.name} de color {player.color} tire el dado...\n")
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

    def action_key_pressed(self, blankparam):
        print(self.current_player.name + "\n")
        #input(f"Presiona Enter para que {self.current_player.name} de color {self.current_player.color} juegue...\n")
        dice_value = self.dice.roll()
        print(f"{self.current_player.name} tiró un {dice_value}.\n")
        jugador_actual_str = ''
        match self.current_player.color:
            case "\033[34mazul\033[00m":
                jugador_actual_str = 'Turno del Jugador: Azul'
            case "\033[31mrojo\033[00m":
                jugador_actual_str = 'Turno del Jugador: Rojo'
            case "\033[32mverde\033[00m":
                jugador_actual_str = 'Turno del Jugador: Verde'
            case "\033[33mamarillo\033[00m":
                jugador_actual_str = 'Turno del Jugador: Amarillo'
        self.board.update_dice_number(dice_value, jugador_actual_str)

        # Implementa la lógica para mover la ficha del jugador actual
        if dice_value == 1 or dice_value == 6:
            if self.current_player.ingresar_ficha()==True and self.current_player.suma_valor_ingame() < 4:
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
                    if player != self.current_player:
                        for ficha_enemiga in player.fichas:
                            if ficha.position == ficha_enemiga.position and ficha_enemiga.final_track == False:
                                print(f"se ha reseteado una ficha de {player.name} por {self.current_player.name}  .\n")
                                ficha_enemiga.reset()

        #ver cuando se corona
        is_coronado = False
        for ficha in self.current_player.fichas:
            if (is_coronado):
                    break
            for comparing_ficha in self.current_player.fichas:
                if (is_coronado):
                    break
                if ficha == comparing_ficha:
                    continue
                else:
                    if ficha.ingame == True and comparing_ficha.ingame == True:
                        if ficha.progress != 0 and comparing_ficha.progress != 0:
                            if ficha.position == comparing_ficha.position:
                                print(f"una ficha de {self.current_player.name} ha sido coronada .\n")
                                ficha.valor += 1
                                comparing_ficha.reset()
                                is_coronado = True
            

        #update board
        self.update_board_state()

        if self.current_player.ganador() == True:
            print(f"{self.current_player.name} es el ganador.\n")
            ganador_text = ''
            match self.current_player.color:
                case "\033[34mazul\033[00m":
                    ganador_text = 'Ganador del Juego: Azul'
                case "\033[31mrojo\033[00m":
                    ganador_text = 'Ganador del Juego: Rojo'
                case "\033[32mverde\033[00m":
                    ganador_text = 'Ganador del Juego: Verde'
                case "\033[33mamarillo\033[00m":
                    ganador_text = 'Ganador del Juego: Amarillo'
            self.board.update_ganador(ganador_text)
            root.unbind('<Return>')
            #declarar ganador

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
        
    def update_board_state(self):
        self.board.remove_pieces()
        for player in self.players:
            print("NOMBRE DE JUGADOR: ", player.name)
            for ficha in player.fichas:
                print("FICHAS DEL JUGADOR: ", ficha.progress)
                #plasmar ficha por ficha en el tablero
                #36 pos es igual al 16 de del tablero
                #pos max 51 --------- 67
                #0 = 32
                if ficha.ingame == True and ficha.valor == 1:
                    match player.color:
                        case "\033[34mazul\033[00m":
                            if ficha.progress <= 35:
                                self.board.add_piece(ficha.progress+32, BoardColor.BLUE, '')
                            elif ficha.progress <= 52:
                                self.board.add_piece(ficha.progress-20, BoardColor.BLUE, '')
                            elif ficha.progress <= 58:
                                self.board.add_piece(ficha.progress+21, BoardColor.BLUE, '')
                        case "\033[31mrojo\033[00m":
                            if ficha.progress <= 22:
                                self.board.add_piece(ficha.progress+45, BoardColor.RED, '')
                            elif ficha.progress <= 52:
                                self.board.add_piece(ficha.progress-7, BoardColor.RED, '')
                            elif ficha.progress <= 58:
                                self.board.add_piece(ficha.progress+27, BoardColor.RED, '')
                        case "\033[32mverde\033[00m":
                            if ficha.progress <= 9:
                                self.board.add_piece(ficha.progress+58, BoardColor.GREEN, '')
                            elif ficha.progress <= 52:
                                self.board.add_piece(ficha.progress+6, BoardColor.GREEN, '')
                            elif ficha.progress <= 58:
                                self.board.add_piece(ficha.progress+33, BoardColor.GREEN, '')
                        case "\033[33mamarillo\033[00m":
                            if ficha.progress <= 48:
                                self.board.add_piece(ficha.progress+19, BoardColor.YELLOW, '')
                            elif ficha.progress <= 52:
                                self.board.add_piece(ficha.progress-32, BoardColor.YELLOW, '')
                            elif ficha.progress <= 58:
                                self.board.add_piece(ficha.progress+15, BoardColor.YELLOW, '')

                if ficha.ingame == True and ficha.valor >= 2:
                    match player.color:
                        case "\033[34mazul\033[00m":
                            if ficha.progress <= 35:
                                self.board.add_piece(ficha.progress+32, BoardColor.BLUE, 'magenta')
                            elif ficha.progress <= 52:
                                self.board.add_piece(ficha.progress-20, BoardColor.BLUE, 'magenta')
                            elif ficha.progress <= 58:
                                self.board.add_piece(ficha.progress+21, BoardColor.BLUE, 'magenta')
                        case "\033[31mrojo\033[00m":
                            if ficha.progress <= 22:
                                self.board.add_piece(ficha.progress+45, BoardColor.RED, 'magenta')
                            elif ficha.progress <= 52:
                                self.board.add_piece(ficha.progress-7, BoardColor.RED, 'magenta')
                            elif ficha.progress <= 58:
                                self.board.add_piece(ficha.progress+27, BoardColor.RED, 'magenta')
                        case "\033[32mverde\033[00m":
                            if ficha.progress <= 9:
                                self.board.add_piece(ficha.progress+58, BoardColor.GREEN, 'magenta')
                            elif ficha.progress <= 52:
                                self.board.add_piece(ficha.progress+6, BoardColor.GREEN, 'magenta')
                            elif ficha.progress <= 58:
                                self.board.add_piece(ficha.progress+33, BoardColor.GREEN, 'magenta')
                        case "\033[33mamarillo\033[00m":
                            if ficha.progress <= 48:
                                self.board.add_piece(ficha.progress+19, BoardColor.YELLOW, 'magenta')
                            elif ficha.progress <= 52:
                                self.board.add_piece(ficha.progress-32, BoardColor.YELLOW, 'magenta')
                            elif ficha.progress <= 58:
                                self.board.add_piece(ficha.progress+15, BoardColor.YELLOW, 'magenta')

    def printInput(self):
        self.playerbase = entry.get()
        self.initialize_players(self.playerbase)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x640")
    root.maxsize(1000,640)
    root.minsize(1000,640)
    root.title('Ludo')

    game = Game(root)

    root.bind('<Return>', game.action_key_pressed)
    initTK = tk.Tk()
    initTK.geometry("300x200")
    entry= Entry(initTK, width= 40)
    entry.focus_set()
    entry.pack()
  
    ttk.Button(initTK, text= "Número de Jugadores",width= 20, command=lambda: [game.printInput(), initTK.destroy()]).pack(pady=20)

    root.mainloop()





