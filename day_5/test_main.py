import unittest
import main
import textwrap


class GivenTestCasePartOne(unittest.TestCase):
    def setUp(self):
        main.DIAGONALS_ENABLED = False
        self.pairs = [
            (main.Point(*p1), main.Point(*p2))
            for p1, p2 in
            [
                ((0, 9), (5, 9)),
                ((8, 0), (0, 8)),
                ((9, 4), (3, 4)),
                ((2, 2), (2, 1)),
                ((7, 0), (7, 4)),
                ((6, 4), (2, 0)),
                ((0, 9), (2, 9)),
                ((3, 4), (1, 4)),
                ((0, 0), (8, 8)),
                ((5, 5), (8, 2))
            ]
        ]
        self.grid = main.Grid(10)

    def test_iterate_to(self):
        expected = [
            [main.Point(*p) for p in [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]],
            None,
            [main.Point(*p) for p in [(9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (4, 4), (3, 4)]],
            [main.Point(*p) for p in [(2, 2), (2, 1)]],
            [main.Point(*p) for p in [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]],
            None,
            [main.Point(*p) for p in [(0, 9), (1, 9), (2, 9)]],
            [main.Point(*p) for p in [(3, 4), (2, 4), (1, 4)]],
            None,
            None
        ]

        for e, p in zip(expected, self.pairs):
            p1, p2 = p
            output = list(p1.iterate_to(p2))
            if e:
                if output != e:
                    output = output[::-1]
                self.assertEqual(e, output)

    def test_mark(self):
        expected = textwrap.dedent("""\
            .......1..
            ..1....1..
            ..1....1..
            .......1..
            .112111211
            ..........
            ..........
            ..........
            ..........
            222111....""")
        for points in self.pairs:
            p1, p2 = points
            for pt in p1.iterate_to(p2):
                if pt:
                    self.grid.mark(pt)

        self.assertEqual(expected, repr(self.grid))

    def test_count(self):
        for points in self.pairs:
            p1, p2 = points
            for pt in p1.iterate_to(p2):
                if pt:
                    self.grid.mark(pt)
        self.assertEqual(self.grid.count(), 5)


class GivenTestCasePartTwo(unittest.TestCase):
    def setUp(self):
        main.DIAGONALS_ENABLED = True
        self.pairs = [
            (main.Point(*p1), main.Point(*p2))
            for p1, p2 in
            [
                ((0, 9), (5, 9)),
                ((8, 0), (0, 8)),
                ((9, 4), (3, 4)),
                ((2, 2), (2, 1)),
                ((7, 0), (7, 4)),
                ((6, 4), (2, 0)),
                ((0, 9), (2, 9)),
                ((3, 4), (1, 4)),
                ((0, 0), (8, 8)),
                ((5, 5), (8, 2))
            ]
        ]
        self.grid = main.Grid(10)

    def test_iterate_to(self):
        expected = [
            [main.Point(*p) for p in [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]],
            [main.Point(*p) for p in [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)]],
            [main.Point(*p) for p in [(9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (4, 4), (3, 4)]][::-1],
            [main.Point(*p) for p in [(2, 2), (2, 1)]],
            [main.Point(*p) for p in [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]],
            [main.Point(*p) for p in [(6, 4), (5, 3), (4, 2), (3, 1), (2, 0)]],
            [main.Point(*p) for p in [(0, 9), (1, 9), (2, 9)]],
            [main.Point(*p) for p in [(3, 4), (2, 4), (1, 4)]],
            [main.Point(*p) for p in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]],
            [main.Point(*p) for p in [(5, 5), (6, 4), (7, 3), (8, 2)]]
        ]

        for e, p in zip(expected, self.pairs):
            p1, p2 = p
            output = list(p1.iterate_to(p2))
            if e != output:
                output = output[::-1]
            self.assertEqual(e, output)

    def test_mark(self):
        expected = textwrap.dedent("""\
            1.1....11.
            .111...2..
            ..2.1.111.
            ...1.2.2..
            .112313211
            ...1.2....
            ..1...1...
            .1.....1..
            1.......1.
            222111....""")
        for points in self.pairs:
            p1, p2 = points
            for pt in p1.iterate_to(p2):
                self.grid.mark(pt)

        self.assertEqual(expected, repr(self.grid))

    def test_count(self):
        for points in self.pairs:
            p1, p2 = points
            for pt in p1.iterate_to(p2):
                self.grid.mark(pt)
        self.assertEqual(self.grid.count(), 12)
