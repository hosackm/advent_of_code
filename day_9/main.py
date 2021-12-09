def gen_neighbors(grid, x, y):
    h = len(grid)
    w = len(grid[0])
    return [(x, y) for x, y in ((x, y-1), (x-1, y), (x+1, y), (x, y+1))
            if x >= 0 and x < w and y >= 0 and y < h]


def find_basin(grid, x, y, basin=None):
    if basin is None:
        basin = set()

    if grid[y][x] == "9":
        return basin

    basin.add((x, y))
    [   # repeat for all neighbors
        find_basin(grid, xn, yn, basin)
        for xn, yn in gen_neighbors(grid, x, y)
        if (xn, yn) not in basin
    ]
    return basin


def find_lowpoints(rows):
    width, height = len(rows[0]), len(rows)
    lowpoints = []
    for i in range(width):
        for j in range(height):
            lowpoint = True  # assume a lowpoint unless proven otherwise
            neighbors = [(i, j-1), (i-1, j), (i+1, j), (i, j+1)]
            for neighbor in neighbors:
                x, y = neighbor
                if x < 0 or x >= width:
                    continue
                if y < 0 or y >= height:
                    continue

                if int(rows[j][i]) >= int(rows[y][x]):
                    lowpoint = False
                    break

            if lowpoint:
                lowpoints.append((i, j, int(rows[j][i])))

    return lowpoints


if __name__ == "__main__":
    with open("input.txt") as f:
        rows = [ln.strip() for ln in f.readlines()]

    # part one
    lps = find_lowpoints(rows)
    print(sum(lp[2]+1 for lp in lps))

    # part two
    basins = [find_basin(rows, lp[0], lp[1]) for lp in lps]
    top_three = sorted([len(s) for s in basins], reverse=True)[:3]
    print(top_three)
