ROW_COUNT = 6
COLUMN_COUNT = 7

class Board:
    def __init__(self):
        self.__lines = ROW_COUNT
        self.__columns = COLUMN_COUNT
        self.__board = self.__create_board()


    def get_value_from_position(self,row,column):
        return self.__board[row][column]

    def checkPosition(self,row,column,value):
        if self.__board[row][column] == value:
            return True
        else:
            return False

    def __create_board(self):
        finalList = []
        lineVector = [0,0,0,0,0,0,0]
        for i in range (0, ROW_COUNT):
            finalList.append(lineVector[:])
        return finalList

    def set_value(self,givenLine,givenColumn,value):
        self.__board[givenLine][givenColumn] = value

    def get_column_values(self,column):
        newVector = []
        for i in range(0,len(self.__board)):
            newVector.append(self.__board[i][column-1])
        return newVector

    def next_empty_line_in_a_column(self,column):
        higherOrderLine = -1
        column_values = self.get_column_values(column)
        for i in range(0,len(column_values)):
            if column_values[i] == 0:
                higherOrderLine = i

        return higherOrderLine

    def is_there_a_possible_move(self):
        column_count = 1
        isPossibleMove = False
        while column_count < 8:
            line_value = self.get_column_values(column_count)
            if line_value[0] == 0:
                isPossibleMove = True
            column_count = column_count + 1

        return isPossibleMove

    def is_move_possible(self,row,column):
        column_values = self.get_column_values(column+1)
        if row+1 <= 5 and (column_values[row+1] == 1 or column_values[row+1] == 2):
            if column_values[row] == 0:
                return True

        return False
