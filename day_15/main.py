from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heappush(self.elements, (priority, item))

    def pop(self):
        return heappop(self.elements)[1]


class Graph:
    def __init__(self, input):
        self.grid = [[0 for _ in row] for row in input.split("\n")]
        for y, line in enumerate(input.split("\n")):
            for x, char in enumerate(line):
                self.grid[y][x] = int(char)

    def __repr__(self):
        return "\n".join("".join(str(n) for n in row) for row in self.grid)

    def all_nodes(self):
        return [(i, j) for j in range(len(self.grid)) for i in range(len(self.grid[0]))]

    def get_neighbors(self, point):
        x, y = point
        neighbors = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
        return [
            (x, y) for x, y in neighbors
            if x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid)
        ]

    def expand_full_board(self):
        out = []
        for row in self.grid:
            new_row = row[:]
            for i in range(1, 5):
                new_row += [n+i for n in row]
            out.append([n - 9 if n > 9 else n for n in new_row])

        tmp = out[:][:]
        for i in range(1, 5):
            out += [[n+i if n+i <= 9 else n+i-9 for n in row] for row in tmp]

        self.grid = out

    def shortest_path(self, start=None, goal=None):
        start = (0, 0) if start is None else start
        goal = (len(self.grid[0])-1, len(self.grid)-1) if goal is None else goal

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.pop()

            if current == goal:
                break

            for nxt in self.get_neighbors(current):
                x, y = nxt
                new_cost = cost_so_far[current] + self.grid[y][x]
                if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                    cost_so_far[nxt] = new_cost
                    priority = new_cost
                    frontier.put(nxt, priority)
                    came_from[nxt] = current

        # reconstruct the path
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path

    def a_star_search(self, start=None, goal=None):
        def heuristic(a, b) -> float:
            (x1, y1) = a
            (x2, y2) = b
            return abs(x1 - x2) + abs(y1 - y2)

        start = (0, 0) if start is None else start
        goal = (len(self.grid[0])-1, len(self.grid)-1) if goal is None else goal
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.pop()
            if current == goal:
                break
            for next in self.get_neighbors(current):
                x, y = next
                new_cost = cost_so_far[current] + self.grid[y][x]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(next, goal)
                    frontier.put(next, priority)
                    came_from[next] = current

        # return came_from, cost_so_far
        # reconstruct the path
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path


if __name__ == "__main__":
    with open("input.txt") as f:
        g = Graph(f.read())

        def sum_path(g, p):
            return sum(g[y][x] if (x, y) != (0, 0) else 0 for x, y in p)

        # part one
        path = g.shortest_path()
        print(sum_path(g.grid, path))

        # part two
        g.expand_full_board()
        path = g.shortest_path()
        print(sum_path(g.grid, path))
