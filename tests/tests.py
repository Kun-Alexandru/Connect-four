from board.board import *
import unittest
from game.game import *
from player.computer import *
from player.human import *
from strategy.noStrategy import *
from strategy.strategy import *

class BoardTests(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board()

    def test_check_position__correct_value_for_position__True(self):
        self.assertTrue(self._board.checkPosition(3,3,0))

    def test_check_position__incorrect_value_for_position__False(self):
        self.assertFalse(self._board.checkPosition(3,3,1))

    def test_set_value__correct_input__correct_value_for_position(self):
        self._board.set_value(3,3,2)
        self.assertTrue(self._board.checkPosition(3,3,2))

    def test_get_column_values__existing_column__correct_column_values(self):
        self._board.set_value(5, 2, 1)
        self._board.set_value(4, 2, 2)
        self._board.set_value(3, 2, 3)
        self._board.set_value(2, 2, 4)
        column_values = self._board.get_column_values(3)
        self.assertEqual(column_values,[0,0,4,3,2,1])

    def test_next_empty_line_in_a_column__existing_column__highest_index_empty_row(self):
        self._board.set_value(5, 2, 1)
        self._board.set_value(4, 2, 2)
        self._board.set_value(3, 2, 3)
        self._board.set_value(2, 2, 4)
        self.assertEqual(self._board.next_empty_line_in_a_column(3),1)


    def test_is_there_an_existing_move__board_with_atleast_1_zero_value__True(self):
        self.assertTrue(self._board.is_there_a_possible_move())

    def test_is_move_possible__non_possible_move__False(self):
        self.assertFalse(self._board.is_move_possible(1,2))

    def test_is_move_possible__possible_move__True(self):
        self._board.set_value(5, 2, 1)
        self._board.set_value(4, 2, 1)
        self._board.set_value(3, 2, 1)
        self._board.set_value(2, 2, 1)
        self.assertTrue(self._board.is_move_possible(1,2))

