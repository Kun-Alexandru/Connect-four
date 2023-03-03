import random
from board.board import *
class NoStrategy():
    def move_computer(self, board):
        moveMade = False
        while moveMade == False:
            column = random.randint(1,7)
            lowestLineInColumn = board.next_empty_line_in_a_column(column)
            if lowestLineInColumn == -1:
                pass
            else:
                board.set_value(lowestLineInColumn, column - 1, 2)
                moveMade = True


