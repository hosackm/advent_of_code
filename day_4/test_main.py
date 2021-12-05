import unittest
from main import Board


class BoardTests(unittest.TestCase):
    def setUp(self):
        size = 5
        self.size = size
        self.b = Board([i for i in range(size*size)])

    def test_mark(self):
        for n in range(self.size*self.size):
            self.assertFalse(self.b.board[n//self.size][n % self.size].marked)
            self.b.mark(n)
            self.assertTrue(self.b.board[n//self.size][n % self.size].marked)

    def test_check(self):
        # starts off not solved
        self.assertFalse(self.b.check())

        # make a row complete
        row = self.b.board[0]
        for s in row:
            s.marked = True

        self.assertTrue(self.b.check())

        # clear board
        for s in row:
            s.marked = False
        self.assertFalse(self.b.check())

        # mark a column as solved
        col = 2
        for row in range(self.size):
            self.b.board[row][col].marked = True
        self.assertTrue(self.b.check())


class GivenTestCase(unittest.TestCase):
    def test_winner(self):
        numbers = [
            7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16,
            13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1
        ]

        board_one = Board([
            22, 13, 17, 11, 0,
            8, 2, 23,  4, 24,
            21, 9, 14, 16,  7,
            6, 10,  3, 18,  5,
            1, 12, 20, 15, 19])

        board_two = Board([
            3, 15,  0,  2, 22,
            9, 18, 13, 17,  5,
            19,  8,  7, 25, 23,
            20, 11, 10, 24,  4,
            14, 21, 16, 12,  6])

        board_three = Board([
            14, 21, 17, 24,  4,
            10, 16, 15,  9, 19,
            18,  8, 23, 26, 20,
            22, 11, 13,  6,  5,
            2,  0, 12,  3,  7])

        for i in range(11):
            n = numbers[i]
            board_one.mark(n)
            board_two.mark(n)
            board_three.mark(n)
            self.assertFalse(board_one.check())
            self.assertFalse(board_two.check())
            self.assertFalse(board_three.check())

        n = numbers[11]  # 24 solves the board 3
        board_one.mark(n)
        board_two.mark(n)
        board_three.mark(n)
        self.assertFalse(board_one.check())
        self.assertFalse(board_two.check())
        self.assertTrue(board_three.check())

        expected_sum = 188
        self.assertEqual(board_three.sum_unmarked(), expected_sum)
