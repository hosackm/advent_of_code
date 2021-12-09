import unittest
from main import find_lowpoints, find_basin


class TestGivenExample(unittest.TestCase):
    def setUp(self):
        self.board = [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678",
        ]

    def test_find_lowpoints(self):
        expected = [
            (1, 0, 1), (9, 0, 0), (2, 2, 5), (6, 4, 5)
        ]
        expected_total = 15
        low_points = find_lowpoints(self.board)
        for e in expected:
            self.assertIn(e, low_points)

        self.assertEqual(sum(lp[2]+1 for lp in low_points), expected_total)

    def test_find_basin(self):
        board = [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678",
        ]
        s = find_basin(board, 1, 0)
        self.assertEqual(len(s), 3)

        s = find_basin(board, 9, 0)
        self.assertEqual(len(s), 9)

        s = find_basin(board, 2, 2)
        self.assertEqual(len(s), 14)

        s = find_basin(board, 6, 4)
        self.assertEqual(len(s), 9)

    def test_find_mult(self):
        board = [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678",
        ]
        lps = find_lowpoints(board)
        basins = [find_basin(board, lp[0], lp[1]) for lp in lps]
        self.assertEqual(len(basins), 4)

        top_three = sorted([len(s) for s in basins], reverse=True)[:3]
        self.assertEqual([14, 9, 9], top_three)
