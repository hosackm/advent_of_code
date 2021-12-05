DIAGONALS_ENABLED = True


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def iterate_to(self, other):
        delta_x, delta_y = 0, 0
        num_pts = max(
            max(self.x, other.x) - min(self.x, other.x) + 1,
            max(self.y, other.y) - min(self.y, other.y) + 1
        )
        if self.x == other.x:
            delta_y = 1 if self.y < other.y else -1
        elif self.y == other.y:
            delta_x = 1 if self.x < other.x else -1
        else:
            delta_x = 1 if self.x < other.x else -1
            delta_y = 1 if self.y < other.y else -1
            if not DIAGONALS_ENABLED:
                yield None
                return

        x, y = self.x, self.y
        for _ in range(num_pts):
            yield Point(x, y)
            x, y = x + delta_x, y + delta_y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Grid:
    def __init__(self, sz=1000):
        self.grid = [[0]*sz for _ in range(sz)]

    def mark(self, point):
        self.grid[point.y][point.x] += 1

    def __repr__(self):
        return "\n".join("".join([str(n) if n > 0 else "." for n in row]) for row in self.grid)

    def count(self):
        return sum([1 if n > 1 else 0 for row in self.grid for n in row])


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = [ln.strip() for ln in f.readlines()]

    points = []
    for line in lines:
        s1, s2 = [s.strip() for s in line.split("->")]
        p1 = [int(n) for n in s1.split(",")]
        p2 = [int(n) for n in s2.split(",")]
        points.append((Point(*p1), Point(*p2)))

    max_x, max_y = 0, 0
    for p1, p2 in points:
        x = max([p1.x, p2.x])
        y = max([p1.y, p2.y])
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y

    max_sz = max(max_x, max_y)
    g = Grid(sz=max_sz+1)
    for pair in points:
        p1, p2 = pair
        for pt in p1.iterate_to(p2):
            g.mark(pt)

    print(g.count())
