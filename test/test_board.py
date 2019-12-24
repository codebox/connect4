import unittest
from board import Board

VAL = 'X'
OTHER = 'O'

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(7, 6, 4)

    def test_vertical_line(self):
        self.assertEqual(self.board.drop(3, VAL), [])
        self.assertEqual(self.board.drop(3, VAL), [])
        self.assertEqual(self.board.drop(3, VAL), [])
        self.assertEqual(self.board.drop(3, VAL), [4])
        self.assertEqual(self.board.drop(3, VAL), [5])

    def test_horizontal_line(self):
        self.assertEqual(self.board.drop(1, VAL), [])
        self.assertEqual(self.board.drop(2, VAL), [])
        self.assertEqual(self.board.drop(3, VAL), [])
        self.assertEqual(self.board.drop(4, VAL), [4])
        self.assertEqual(self.board.drop(5, VAL), [5])

    def test_diagonal_line(self):
        self.assertEqual(self.board.drop(1, VAL), [])

        self.assertEqual(self.board.drop(2, OTHER), [])
        self.assertEqual(self.board.drop(2, VAL), [])

        self.assertEqual(self.board.drop(3, OTHER), [])
        self.assertEqual(self.board.drop(3, OTHER), [])
        self.assertEqual(self.board.drop(3, VAL), [])

        self.assertEqual(self.board.drop(4, OTHER), [])
        self.assertEqual(self.board.drop(4, OTHER), [])
        self.assertEqual(self.board.drop(4, OTHER), [])
        self.assertEqual(self.board.drop(4, VAL), [4])

    def test_multiple_lines(self):
        self.assertEqual(self.board.drop(1, VAL), [])

        self.assertEqual(self.board.drop(2, OTHER), [])
        self.assertEqual(self.board.drop(2, VAL), [])

        self.assertEqual(self.board.drop(3, OTHER), [])
        self.assertEqual(self.board.drop(3, OTHER), [])
        self.assertEqual(self.board.drop(3, VAL), [])

        self.assertEqual(self.board.drop(4, VAL), [])
        self.assertEqual(self.board.drop(4, VAL), [])
        self.assertEqual(self.board.drop(4, VAL), [])
        self.assertEqual(self.board.drop(4, VAL), [4,4])

    def test_bad_moves(self):
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)

        with self.assertRaises(ValueError):
            self.board.drop(3, VAL)

        with self.assertRaises(ValueError):
            self.board.drop(-1, VAL)

        self.board.drop(0, VAL)
        self.board.drop(6, VAL)

        with self.assertRaises(ValueError):
            self.board.drop(7, VAL)

    def test_valid_moves(self):
        self.assertEqual(self.board.get_valid_moves(), [0,1,2,3,4,5,6])

        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)

        self.assertEqual(self.board.get_valid_moves(), [0,1,2,3,4,5,6])

        self.board.drop(3, VAL)

        self.assertEqual(self.board.get_valid_moves(), [0,1,2,4,5,6])

    def test_reset(self):
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)
        self.board.drop(3, VAL)

        self.assertEqual(self.board.get_valid_moves(), [0,1,2,4,5,6])
        self.board.reset()
        self.assertEqual(self.board.get_valid_moves(), [0,1,2,3,4,5,6])


    def test_board_view(self):
        self.assertEqual(self.board.get_view_for(VAL).to_id(), '....... ....... ....... ....... ....... .......')
        self.board.drop(3, VAL)
        self.assertEqual(self.board.get_view_for(VAL).to_id(), '....... ....... ....... ....... ....... ...X...')
        self.board.drop(3, VAL)
        self.assertEqual(self.board.get_view_for(VAL).to_id(), '....... ....... ....... ....... ...X... ...X...')
        self.board.drop(3, OTHER)
        self.assertEqual(self.board.get_view_for(VAL).to_id(), '....... ....... ....... ...o... ...X... ...X...')

if __name__ == '__main__':
    unittest.main()