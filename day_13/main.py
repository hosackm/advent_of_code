def parse_input(lines):
    marks = []
    folds = []
    is_marks = True
    for line in lines.split("\n"):
        line = line.strip()
        if not line:
            is_marks = False
            continue
        if is_marks:
            x, y = line.split(",")
            marks.append((int(x), int(y)))
        else:
            fold, n = line.split("=")
            folds.append((fold[-1], int(n)))
    return marks, folds


class Origami:
    def __init__(self, marks):
        self.w = max([m[0] for m in marks]) + 1
        self.h = max([m[1] for m in marks]) + 1
        self.grid = [["." for x in range(self.w)] for y in range(self.h)]
        for x, y in marks:
            self.grid[y][x] = "#"

    def num_dots(self):
        return sum(1 if n == "#" else 0 for row in self.grid for n in row)

    def fold_x(self, x):
        """Fold verticaly across an x-axis"""
        new_grid = [row[:x] for row in self.grid]

        for j, row in enumerate(self.grid):
            reflection = row[x:][::-1]
            for i, old in enumerate(reflection):
                if old == "#":
                    new_grid[j][i] = "#"

        self.grid = new_grid
        self.w = x

    def fold_y(self, y):
        """Fold horizontally across a y-axis"""
        new_grid = [row for row in self.grid[:y]]

        for j in range(y+1, self.h):
            for i in range(self.w):
                if self.grid[j][i] == "#":
                    reflect_y = self.h - j - y - 1
                    new_grid[reflect_y][i] = "#"

        self.grid = new_grid
        self.h = y

    def __repr__(self):
        return "\n".join("".join(c for c in row) for row in self.grid)


if __name__ == "__main__":
    with open("input.txt") as f:
        marks, folds = parse_input(f.read())
        o = Origami(marks)

        for i, fold in enumerate(folds):
            direction, n = fold
            if direction == "y":
                o.fold_y(n)
            else:
                o.fold_x(n)

            # part one
            if i == 0:
                print(f"After one fold there are {o.num_dots()} dots")

        # part two
        print(o)
