from board.board import *
from game.game import *
from player.computer import *
from player.human import *
from strategy.noStrategy import *
from strategy.strategy import *

if __name__ == '__main__':
    board = Board()
    strategy = Strategy()
    player1 = Human("You", board)
    player2 = Computer("Computer",board,strategy)
    game = Game(board,player1,player2)

    game.play()