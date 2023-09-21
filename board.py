import tkinter as tk
import random

class BoardSetting:
    SQUARE_SIZE = 40
    BOARD_WIDTH = 640
    BOARD_HEIGHT = 640
    DEBUG = False

class BoardColor:
    GREEN = '#0CED2C'
    RED = '#F71313'
    YELLOW = '#FFFF00'
    BLUE = '#3575EC'
    DEFAULT = '#E9E9E9'
    CYAN = '#4EB1BA'
    GRAY = '#A9A9A9'

class Board:
    def __init__(self, master):
        self.current_dice_number = 0;
        self.canvas = tk.Canvas(master, width=BoardSetting.BOARD_WIDTH, height=BoardSetting.BOARD_HEIGHT, bg="black")
        self.throw_dice_button = tk.Button(master, text='Tirar Dado', command=self.update_dice_number, width=20, height=2)
        self.current_dice_number_label = tk.Label(master, text=str(self.current_dice_number), width=10, height=5, font=("Arial", 40))
        self.home_coordinates_map = {
            0: (82.5, 82.5, 115.5, 115.5),
            1: (82.5, 162.5, 115.5, 195.5),
            2: (162.5, 82.5, 195.5, 115.5),
            3: (162.5, 162.5, 195.5, 195.5),
            4: (82.5, 442.5, 115.5, 475.5),
            5: (82.5, 522.5, 115.5, 555.5),
            6: (162.5, 442.5, 195.5, 475.5),
            7: (162.5, 522.5, 195.5, 555.5),
            8: (442.5, 82.5, 475.5, 115.5),
            9: (442.5, 162.5, 475.5, 195.5),
            10: (522.5, 82.5, 555.5, 115.5),
            11: (522.5, 162.5, 555.5, 195.5),
            12: (442.5, 442.5, 475.5, 475.5),
            13: (442.5, 522.5, 475.5, 555.5),
            14: (522.5, 442.5, 555.5, 475.5),
            15: (522.5, 522.5, 555.5, 555.5)
        }
        self.coordinates_map = {
            16: (6, 0), 17: (7, 0), 18: (8, 0), 19: (8, 1), 20: (8, 2), 
            21: (8, 3), 22: (8, 4), 23: (8, 5), 24: (9, 6), 25: (10, 6), 
            26: (11, 6), 27: (12, 6), 28: (13, 6), 29: (14, 6), 30: (14, 7),
            31: (14, 8), 32: (13, 8), 33: (12, 8), 34: (11, 8), 35: (10, 8),
            36: (9, 8), 37: (8, 9), 38: (8, 10), 39: (8, 11), 40: (8, 12),
            41: (8, 13), 42: (8, 14), 43: (7, 14), 44: (6, 14), 45: (6, 13),
            46: (6, 12), 47: (6, 11), 48: (6, 10), 49: (6, 9), 50: (5, 8),
            51: (4, 8), 52: (3, 8), 53: (2, 8), 54: (1, 8), 55: (0, 8),
            56: (0, 7), 57: (0, 6), 58: (1, 6), 59: (2, 6), 60: (3, 6),
            61: (4, 6), 62: (5, 6), 63: (6, 5), 64: (6, 4), 65: (6, 3),
            66: (6, 2), 67: (6, 1), 68: (7, 1), 69: (7, 2), 70: (7, 3),
            71: (7, 4), 72: (7, 5), 73: (7, 6), 74: (13, 7), 75: (12, 7),
            76: (11, 7), 77: (10, 7), 78: (9, 7), 79: (8, 7), 80: (7, 13),
            81: (7, 12), 82: (7, 11), 83: (7, 10), 84: (7, 9), 85: (7, 8),
            86: (1, 7), 87: (2, 7), 88: (3, 7), 89: (4, 7), 90: (5, 7), 
            91: (6, 7)
        }
        self.pieces = []

    def update_dice_number(self):
        self.current_dice_number = random.randint(1, 6)
        self.current_dice_number_label.config(text=str(self.current_dice_number))


    def draw_rectangle(self, lx, ly, bx, by, color, width):
        self.canvas.create_rectangle(
            lx * BoardSetting.SQUARE_SIZE,
            ly * BoardSetting.SQUARE_SIZE,
            bx * BoardSetting.SQUARE_SIZE,
            by * BoardSetting.SQUARE_SIZE,
            fill=color,
            width = width,
        )

    def draw_polygon(self, x1, y1, x2, y2, color, width):
        self.canvas.create_polygon(
            x1 * BoardSetting.SQUARE_SIZE,
            y1 * BoardSetting.SQUARE_SIZE,
            BoardSetting.BOARD_WIDTH // 2,
            BoardSetting.BOARD_HEIGHT // 2,
            x2 * BoardSetting.SQUARE_SIZE,
            y2 * BoardSetting.SQUARE_SIZE,
            fill=color,
            width=width,
            outline="white"
        )

    def draw_circle(self, x1, y1, x2, y2, color):
        return self.canvas.create_oval(
            x1 * BoardSetting.SQUARE_SIZE,
            y1 * BoardSetting.SQUARE_SIZE,
            x2 * BoardSetting.SQUARE_SIZE,
            y2 * BoardSetting.SQUARE_SIZE,
            fill=color,
        )

    def draw_arrow(self, x1, y1, x2, y2, color, point):
        lx, ly = x1 * BoardSetting.SQUARE_SIZE, y1 * BoardSetting.SQUARE_SIZE
        bx, by = x2 * BoardSetting.SQUARE_SIZE, y2 * BoardSetting.SQUARE_SIZE

        center_x = (lx + bx) / 2
        center_y = (ly + by) / 2

        first_point = None
        second_point = None
        third_point = None

        if point == 'top':
            first_point = (center_x, center_y - 10)
            second_point = (center_x - 10, center_y + 10)
            third_point = (center_x + 10, center_y + 10)


        if point == 'bottom':
            first_point = (center_x, center_y + 10)
            second_point = (center_x - 10, center_y - 10)
            third_point = (center_x + 10, center_y - 10)

        if point == 'right':
            first_point = (center_x + 10, center_y)
            second_point = (center_x - 10, center_y - 10)
            third_point = (center_x - 10, center_y + 10)

        if point == 'left':
            first_point = (center_x - 10, center_y)
            second_point = (center_x + 10, center_y - 10)
            third_point = (center_x + 10, center_y + 10)

        if first_point is None or second_point is None or third_point is None:
            return

        self.canvas.create_polygon(
            first_point,
            second_point,
            third_point,
            fill=color
        )

    def path_numbers(self):
        # Add numbers for each square
        counter = 0

        for x1, x2 in [(1.65, 3.3), (3.65, 5.3)]:
            for y1, y2 in [(1.65, 3.3), (3.65, 5.3)]:
                center_x = (x1 * 40 + x2 * 40) / 2
                center_y = (y1 * 40 + y2 * 40) / 2
                self.canvas.create_text(center_x, center_y, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for x1, x2 in [(1.65, 3.3), (3.65, 5.3)]:
            for y1, y2 in [(10.65, 12.3), (12.65, 14.3)]:
                center_x = (x1 * 40 + x2 * 40) / 2
                center_y = (y1 * 40 + y2 * 40) / 2
                self.canvas.create_text(center_x, center_y, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for x1, x2 in [(10.65, 12.3), (12.65, 14.3)]:
            for y1, y2 in [(1.65, 3.3), (3.65, 5.3)]:
                center_x = (x1 * 40 + x2 * 40) / 2
                center_y = (y1 * 40 + y2 * 40) / 2
                self.canvas.create_text(center_x, center_y, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for x1, x2 in [(10.65, 12.3), (12.65, 14.3)]:
            for y1, y2 in [(10.65, 12.3), (12.65, 14.3)]:
                center_x = (x1 * 40 + x2 * 40) / 2
                center_y = (y1 * 40 + y2 * 40) / 2
                self.canvas.create_text(center_x, center_y, text=str(counter), fill=BoardColor.CYAN)
                counter += 1
        
        for i in range(6, 9):
            j = 0
            self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
            counter += 1

        for i in range(8, 9):
            for j in range(1, 6):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(9, 15):
            j = 6
            self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
            counter += 1

        for i in range(14, 15):
            for j in range(7, 9):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(13, 8, -1):
            j = 8
            self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
            counter += 1

        for i in range(8, 9):
            for j in range(9, 15):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(7, 5, -1):
            j = 14
            self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
            counter += 1

        for i in range(6, 7):
            for j in range(13, 8, -1):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(5, -1, -1):
            j = 8
            self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
            counter += 1

        for i in range(0, 1):
            for j in range(7, 5, -1):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(1, 6):
            j = 6
            self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
            counter += 1

        for i in range(6, 7):
            for j in range(5, 0, -1):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(7, 8):
            for j in range(1, 7):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(13, 7, -1):
            for j in range(7, 8):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(7, 8):
            for j in range(13, 7, -1):
                self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
                counter += 1

        for i in range(1, 7):
            j = 7
            self.canvas.create_text((i + 1) * 40, (j + 1) * 40, text=str(counter), fill=BoardColor.CYAN)
            counter += 1



    def path(self):
        self.canvas.place(x=0, y=0) 
        
        # Draw each square
        for i in range(6, 9):
            for j in range(15):
                if (j not in range(6, 9) and i != 7 or j == 0 or j == 14):
                  self.draw_rectangle(i + 0.5, j + 0.5, i + 1.5, j + 1.5, '', 1)
                  self.draw_rectangle(j + 0.5, i + 0.5, j + 1.5, i + 1.5, '', 1)

                else:
                    if j < 6:
                        self.draw_rectangle(i + 0.5, j + 0.5, i + 1.5, j + 1.5, BoardColor.YELLOW, 1)
                        self.draw_rectangle(j + 0.5, i + 0.5, j + 1.5, i + 1.5, BoardColor.GREEN, 1)
                    elif j > 8:
                        self.draw_rectangle(i + 0.5, j + 0.5, i + 1.5, j + 1.5, BoardColor.RED, 1)
                        self.draw_rectangle(j + 0.5, i + 0.5, j + 1.5, i + 1.5, BoardColor.BLUE, 1) 
        
        # Draw starting square of each player
        self.draw_rectangle(8.5, 1.5, 9.5, 2.5, BoardColor.YELLOW, 1)
        self.draw_rectangle(6.5, 13.5, 7.5, 14.5, BoardColor.RED, 1)
        self.draw_rectangle(1.5, 6.5, 2.5, 7.5, BoardColor.GREEN, 1)
        self.draw_rectangle(13.5, 8.5, 14.5, 9.5, BoardColor.BLUE, 1)

        # Draw arrow indicating where to enter the path for each player
        self.draw_arrow(6.5, 2.5, 7.5, 3.5, BoardColor.YELLOW, 'right')
        self.draw_arrow(8.5, 12.5, 9.5, 13.5, BoardColor.RED, 'left')
        self.draw_arrow(2.5, 8.5, 3.5, 9.5, BoardColor.GREEN, 'top')
        self.draw_arrow(12.5, 6.5, 13.5, 7.5, BoardColor.BLUE, 'bottom')

        # Formulas to draw squares (x and y starting from 0)

        # On the y axis
        # self.draw_rectangle(x + 0.5, y + 0.5, x + 1.5, y + 1.5, Color.YELLOW, 1)

        # On the x axix
        # self.draw_rectangle(y + 0.5, x + 0.5, y + 1.5, x + 1.5, Color.GREEN, 1)

    def home(self):
        # Draw big squares for each home
        self.draw_rectangle(0.5, 0.5, 6.5, 6.5, BoardColor.GREEN, 3)
        self.draw_rectangle(0.5, 9.5, 6.5, 15.5, BoardColor.RED, 3)
        self.draw_rectangle(9.5, 0.5, 15.5, 6.5, BoardColor.YELLOW, 3)
        self.draw_rectangle(9.5, 9.5, 15.5, 15.5, BoardColor.BLUE, 3)
        self.draw_rectangle(1.25, 1.25, 5.75, 5.75, BoardColor.DEFAULT, 0)
        self.draw_rectangle(1.25, 10.25, 5.75, 14.75, BoardColor.DEFAULT, 0)
        self.draw_rectangle(10.25, 1.25, 14.75, 5.75, BoardColor.DEFAULT, 0)
        self.draw_rectangle(10.25, 10.25, 14.75, 14.75, BoardColor.DEFAULT, 0)
            
        # Draw small squares for each piece starting point
        self.draw_rectangle(1.65, 1.65, 3.3, 3.3, BoardColor.GREEN, 0)
        self.draw_rectangle(3.65, 3.65, 5.3, 5.3, BoardColor.GREEN, 0)
        self.draw_rectangle(1.65, 3.65, 3.3, 5.3, BoardColor.GREEN, 0)
        self.draw_rectangle(3.65, 1.65, 5.3, 3.3, BoardColor.GREEN, 0)

        self.draw_rectangle(1.65, 10.65, 3.3, 12.3, BoardColor.RED, 0)
        self.draw_rectangle(3.65, 12.65, 5.3, 14.3, BoardColor.RED, 0)
        self.draw_rectangle(1.65, 12.65, 3.3, 14.3, BoardColor.RED, 0)
        self.draw_rectangle(3.65, 10.65, 5.3, 12.3, BoardColor.RED, 0)

        self.draw_rectangle(10.65, 1.65, 12.3, 3.3, BoardColor.YELLOW, 0)
        self.draw_rectangle(12.65, 3.65, 14.3, 5.3, BoardColor.YELLOW, 0)
        self.draw_rectangle(10.65, 3.65, 12.3, 5.3, BoardColor.YELLOW, 0)
        self.draw_rectangle(12.65, 1.65, 14.3, 3.3, BoardColor.YELLOW, 0)

        self.draw_rectangle(10.65, 10.65, 12.3, 12.3, BoardColor.BLUE, 0)
        self.draw_rectangle(12.65, 12.65, 14.3, 14.3, BoardColor.BLUE, 0)
        self.draw_rectangle(10.65, 12.65, 12.3, 14.3, BoardColor.BLUE, 0)
        self.draw_rectangle(12.65, 10.65, 14.3, 12.3, BoardColor.BLUE, 0)
        
        # Draw arrows on the center of the board
        self.draw_polygon(6.5, 6.5, 6.5, 9.5, BoardColor.GREEN, 1)
        self.draw_polygon(6.5, 6.5, 9.5, 6.5, BoardColor.YELLOW, 1)
        self.draw_polygon(9.5, 9.5, 6.5, 9.5, BoardColor.RED, 1)
        self.draw_polygon(9.5, 9.5, 9.5, 6.5, BoardColor.BLUE, 1)

    def create(self):
        self.path()
        self.home()

        self.throw_dice_button.place(x=715, y=400)
        self.current_dice_number_label.place(x=710, y=100)

        if BoardSetting.DEBUG:
            self.path_numbers() 

    def add_piece(self, number, color):
        if number < 16:
            x1, y1, x2, y2 = self.home_coordinates_map.get(number, (0, 0, 0, 0))
            piece = self.canvas.create_oval(x1, y1, x2, y2, fill=color)
            self.pieces.append(piece)
        else:
            x, y = self.coordinates_map.get(number, (0, 0))
            piece = self.draw_circle(x + 0.7, y + 0.7, x + 1.3, y + 1.3, color)
            self.pieces.append(piece)

    def remove_pieces(self):
        for piece in self.pieces:
            self.canvas.delete(piece)

        self.pieces = []

    def get_canvas(self):
        return self.canvas
