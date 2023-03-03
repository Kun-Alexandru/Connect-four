ROW_COUNT = 6
COLUMN_COUNT = 7
import random

class Strategy():

    def checkLine(self,player_value,board):

        for column in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT):
                if board.checkPosition(row, column, player_value) == True and board.checkPosition(row, column + 1,player_value) == True and board.checkPosition(row,column + 2,player_value) == True and board.checkPosition(row, column + 3, 0) == True:
                    if board.is_move_possible(row, column + 3) == True:
                        board.set_value(row, column + 3, 2)
                        return True
                elif board.checkPosition(row, column, player_value) == True and board.checkPosition(row, column + 1,player_value) == True and board.checkPosition(row,column + 2,0) == True and board.checkPosition(row, column + 3, player_value) == True:
                    if board.is_move_possible(row, column + 2) == True:
                        board.set_value(row, column + 2, 2)
                        return True
                elif board.checkPosition(row, column, player_value) == True and board.checkPosition(row, column + 1,0) == True and board.checkPosition(row,column + 2,player_value) == True and board.checkPosition(row, column + 3, player_value) == True:
                    if board.is_move_possible(row, column + 1) == True:
                        board.set_value(row, column + 1, 2)
                        return True
                elif board.checkPosition(row, column, 0) == True and board.checkPosition(row - 1, column + 1,player_value) == True and board.checkPosition(row - 2, column + 2, player_value) == True and board.checkPosition(row - 3, column + 3, player_value) == True:
                    if board.is_move_possible(row, column) == True:
                        board.set_value(row, column, 2)
                        return True

        return False

    def checkColumn(self,player_value,board):

        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT - 3):
                if board.checkPosition(row, column, player_value) == True and board.checkPosition(row + 1, column,player_value) == True and board.checkPosition(row + 2, column, player_value) == True and board.checkPosition(row + 3, column, 0) == True:
                    if board.is_move_possible(row + 3, column) == True:
                        board.set_value(row + 3, column, 2)
                        return True
                elif board.checkPosition(row, column, player_value) == True and board.checkPosition(row + 1, column,player_value) == True and board.checkPosition(row + 2, column, 0) == True and board.checkPosition(row + 3, column, player_value) == True:
                    if board.is_move_possible(row + 2, column) == True:
                        board.set_value(row + 2, column, 2)
                        return True
                elif board.checkPosition(row, column, player_value) == True and board.checkPosition(row + 1, column,0) == True and board.checkPosition(row + 2, column, player_value) == True and board.checkPosition(row + 3, column, player_value) == True:
                    if board.is_move_possible(row + 1, column) == True:
                        board.set_value(row + 1, column, 2)
                        return True
                elif board.checkPosition(row, column, 0) == True and board.checkPosition(row + 1, column,player_value) == True and board.checkPosition(row + 2, column, player_value) == True and board.checkPosition(row + 3, column, player_value) == True:
                    if board.is_move_possible(row, column) == True:
                        board.set_value(row, column, 2)
                        return True

        return False
    def checkDiagonal(self,player_value,board):
        for column in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT - 3):
                if board.checkPosition(row, column, player_value) == True and board.checkPosition(row + 1, column + 1,player_value) == True and board.checkPosition(row + 2, column + 2, player_value) == True and board.checkPosition(row + 3, column + 3, 0) == True:
                    if board.is_move_possible(row + 3, column + 3) == True:
                        board.set_value(row + 3, column + 3, 2)
                        return True
                elif board.checkPosition(row, column, player_value) == True and board.checkPosition(row + 1, column + 1,player_value) == True and board.checkPosition(row + 2, column + 2, 0) == True and board.checkPosition(row + 3, column + 3, player_value) == True:
                    if board.is_move_possible(row + 2, column + 2) == True:
                         board.set_value(row + 2, column + 2, 2)
                         return True
                elif board.checkPosition(row, column, player_value) == True and board.checkPosition(row + 1, column + 1,0) == True and board.checkPosition(row + 2, column + 2, player_value) == True and board.checkPosition(row + 3, column + 3, player_value) == True:
                    if board.is_move_possible(row + 1, column + 1) == True:
                        board.set_value(row + 1, column + 1, 2)
                        return True
                if board.checkPosition(row, column, 0) == True and board.checkPosition(row + 1, column + 1,player_value) == True and board.checkPosition(row + 2, column + 2, player_value) == True and board.checkPosition(row + 3, column + 3, player_value) == True:
                    if board.is_move_possible(row, column) == True:
                        board.set_value(row, column, 2)
                        return True
        return False
    def check2ndDiagonal(self,player_value,board):
        for column in range(COLUMN_COUNT - 3):
            for row in range(3, ROW_COUNT):
                if board.checkPosition(row, column, player_value) == True and board.checkPosition(row - 1, column + 1,player_value) == True and board.checkPosition(row - 2, column + 2, player_value) == True and board.checkPosition(row - 3, column + 3, 0) == True:
                    if board.is_move_possible(row - 3, column + 3) == True:
                        board.set_value(row - 3, column + 3, 2)
                        return True
                if board.checkPosition(row, column, player_value) == True and board.checkPosition(row - 1, column + 1,player_value) == True and board.checkPosition(row - 2, column + 2, 0) == True and board.checkPosition(row - 3, column + 3, player_value) == True:
                    if board.is_move_possible(row - 2, column + 2) == True:
                        board.set_value(row - 2, column + 2, 2)
                        return True
                if board.checkPosition(row, column, player_value) == True and board.checkPosition(row - 1, column + 1,0) == True and board.checkPosition(row - 2, column + 2, player_value) == True and board.checkPosition(row - 3, column + 3, player_value) == True:
                    if board.is_move_possible(row - 1, column + 1) == True:
                        board.set_value(row - 1, column + 1, 2)
                        return True
                if board.checkPosition(row, column, 0) == True and board.checkPosition(row - 1, column + 1,player_value) == True and board.checkPosition(row - 2, column + 2, player_value) == True and board.checkPosition(row - 3, column + 3, player_value) == True:
                    if board.is_move_possible(row, column) == True:
                        board.set_value(row, column, 2)
                        return True
        return False


    def move_computer(self, board):

        moveMade = False
        human_code = 1
        computer_code = 2
        if moveMade == False:
            moveMade = self.checkLine(computer_code,board)

        if moveMade == False:
            moveMade = self.checkLine(human_code,board)

        if moveMade == False:
            moveMade = self.checkColumn(computer_code,board)

        if moveMade == False:
            moveMade = self.checkColumn(human_code,board)

        if moveMade == False:
            moveMade = self.checkDiagonal(computer_code,board)

        if moveMade == False:
            moveMade = self.checkDiagonal(human_code,board)

        if moveMade == False:
            moveMade = self.check2ndDiagonal(computer_code,board)

        if moveMade == False:
            moveMade = self.check2ndDiagonal(human_code,board)


        while moveMade == False:
            column = random.randint(1,7)
            lowestLineInColumn = board.next_empty_line_in_a_column(column)
            if lowestLineInColumn == -1:
                pass
            else:
                board.set_value(lowestLineInColumn, column - 1, 2)
                moveMade = True




