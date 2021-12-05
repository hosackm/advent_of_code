from dataclasses import dataclass


@dataclass
class GridSpot:
    num: int
    marked: bool = False


class Board:
    def __init__(self, numbers, size=5):
        self.solved = False
        self.size = size
        self.board = [[GridSpot(0)]*size for _ in range(size)]
        self._place_numbers(numbers)

    def _place_numbers(self, numbers):
        for row in range(self.size):
            for col in range(self.size):
                n = numbers[row*self.size+col]
                self.board[row][col] = GridSpot(n)

    def mark(self, num):
        for spot in range(self.size*self.size):
            sp = self.board[spot//self.size][spot % self.size]
            if sp.num == num:
                sp.marked = True

    def check(self):
        # check horizontal
        for row in range(self.size):
            if all(s.marked for s in self.board[row]):
                self.solved = True
                return True

        # check vertical
        for col in range(self.size):
            vert = [row[col] for row in self.board]
            if all(s.marked for s in vert):
                self.solved = True
                return True

        return False

    def sum_unmarked(self):
        return sum([n.num if not n.marked else 0 for row in self.board for n in row])

    def __repr__(self):
        return "\n".join([" ".join([f"{n.num:2d}" for n in row]) for row in self.board])


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()

    called_numbers = [int(n) for n in lines[0].split(",")]

    # \n and then 5 lines of numbers
    number_groups = []
    current_numbers = []
    num_lines = len(lines)
    i = 1
    while i < num_lines:
        if lines[i] == "\n":
            if current_numbers:
                number_groups.append(current_numbers)
                current_numbers = []
            i += 1
            continue
        current_numbers += [int(n) for n in lines[i].strip().split()]
        i += 1

    boards = []
    solved = []
    for group in number_groups:
        boards.append(Board(group))

    for n in called_numbers:
        for i, b in enumerate(boards):
            if b.solved:
                continue

            b.mark(n)
            if b.check():
                solved.append(b)
                s = b.sum_unmarked()
                print(f"Board {i} solved with number: {n}")
                print(f"Sum of unmarked: {s}")
                print(f"s*n = {s*n}")
                print("-"*80)
