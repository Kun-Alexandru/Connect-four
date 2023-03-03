from player.player import *
from board.board import *

class Computer(Player):
    def __init__(self, name, board, strategy):
        super().__init__(name, board)
        self.__strategy = strategy

    def move(self):
        return self.__strategy.move_computer(self._board)
