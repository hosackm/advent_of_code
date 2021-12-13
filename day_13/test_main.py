from textwrap import dedent
from main import parse_input, Origami


def test_simple_example():
    input_lines = dedent("""\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""")
    expected_marks = [
        (6, 10), (0, 14), (9, 10), (0, 3), (10, 4), (4, 11),
        (6, 0), (6, 12), (4, 1), (0, 13), (10, 12), (3, 4),
        (3, 0), (8, 4), (1, 10), (2, 14), (8, 10), (9, 0),
    ]
    expected_folds = [("y", 7), ("x", 5)]
    marks, folds = parse_input(input_lines)
    for mark in expected_marks:
        assert mark in marks
    for fold in expected_folds:
        assert fold in folds

    o = Origami(marks)
    for mark in expected_marks:
        x, y = mark
        assert o.grid[y][x] == "#"

    grid_after = [
        ["#", ".", "#", "#", ".", ".", "#", ".", ".", "#", "."],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
        [".", "#", ".", "#", ".", ".", "#", ".", "#", "#", "#"],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    o.fold_y(7)
    assert o.h == 7
    assert o.grid == grid_after
    assert o.num_dots() == 17

    grid_after = [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#"],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
    ]
    o.fold_x(5)
    assert o.w == 5
    assert o.grid == grid_after
    assert o.num_dots() == 16
