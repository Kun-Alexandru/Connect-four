from board.board import *
from player.human import *
from player.computer import *
ROW_COUNT = 6
COLUMN_COUNT = 7

class ColumnException(Exception):
    pass

class Game:
    def __init__(self, board, player1, player2):
        self.__board = board
        self.__player1 = player1
        self.__player2 = player2

    def play(self):
        while True:
            if self.__move(self.__player1, 1) == True:
                self.__show_game_over_status()
                break
            if self.__move(self.__player2, 2) == True:
                self.__show_game_over_status()
                break

    def __read_data(self):
        givenColumn = input("Give the column in which you want to place the next piece (>=1 & <=7)")

        if(givenColumn.isnumeric() == False):
            raise ColumnException("Invalid column given")

        if(int(givenColumn) < 1 or int(givenColumn) > 7):
            raise ColumnException("Invalid column given")

        givenColumn = int(givenColumn)

        return givenColumn, True

    def print_board(self):
        for i in range(0, ROW_COUNT):
            for j in range(0, COLUMN_COUNT):
                print(str(self.__board.get_value_from_position(i,j)), end ="  ")
            print("")

    def __move(self,player,value):
        if type(player) == Human:
            self.print_board()
            openRow = False
            while openRow == False:
                openRow = False
                correctRead = False
                while correctRead == False:
                    try:
                        column,correctRead = self.__read_data()
                    except ColumnException as ce:
                        self.print_board()
                        print(ce)
                lowestLineInColumn = self.__board.next_empty_line_in_a_column(column)
                if lowestLineInColumn == -1:
                    print("This column is already full")
                else:
                    self.__board.set_value(lowestLineInColumn,column-1,value)
                    openRow = True

        else:
            self.__player2.move()

        if self.__board.is_there_a_possible_move() == False or self.board_has_winner_move(1) == True or self.board_has_winner_move(2) == True:
            return True

        return False

    def board_has_winner_move(self, value):
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if self.__board.checkPosition(r,c,value) == True and self.__board.checkPosition(r,c+1,value) == True and self.__board.checkPosition(r,c+2,value) == True and self.__board.checkPosition(r,c+3,value) == True:
                    return True

            # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.__board.checkPosition(r, c, value) == True and self.__board.checkPosition(r+1, c ,value) == True and self.__board.checkPosition(r+2, c , value) == True and self.__board.checkPosition(r+3, c , value) == True:
                    return True

            # Check positively sloped diaganols
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if self.__board.checkPosition(r, c, value) == True and self.__board.checkPosition(r+1, c + 1,value) == True and self.__board.checkPosition(r+2, c + 2, value) == True and self.__board.checkPosition(r+3, c + 3, value) == True:
                    return True

            # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if self.__board.checkPosition(r, c, value) == True and self.__board.checkPosition(r-1, c + 1,value) == True and self.__board.checkPosition(r-2, c + 2, value) == True and self.__board.checkPosition(r-3, c + 3, value) == True:
                    return True

        return False

    def __show_game_over_status(self):
        self.print_board()
        print("game over")



