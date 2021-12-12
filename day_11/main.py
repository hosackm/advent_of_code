class Grid:
    def __init__(self, nums):
        self.nums = nums
        self.w = len(self.nums[0])
        self.h = len(self.nums)
        self.flashed = [[False for _ in range(self.w)] for _ in range(self.h)]
        self.count = 0

    def __repr__(self):
        return "\n".join(
            "".join(str(n) for n in row)
            for row in self.nums)

    def __eq__(self, other):
        for x, y in [(i, j) for i in range(self.w) for j in range(self.h)]:
            if self.nums[y][x] != other.nums[y][x]:
                return False
        return True

    def tick(self):
        flashers = set()
        for x, y in [(i, j) for i in range(self.w) for j in range(self.h)]:
            self.nums[y][x] += 1
            if self.nums[y][x] > 9:
                flashers.add((x, y))

        self.flash(flashers)
        self.reset()

    def flash(self, flashers):
        while flashers:
            fx, fy = flashers.pop()
            if self.flashed[fy][fx]:
                continue

            # flash this octopus
            self.flashed[fy][fx] = True
            self.count += 1

            neighbors = [
               (fx+d2, fy+d1)
               for d1 in range(-1, 2) for d2 in range(-1, 2)
               if not (d1 == 0 and d2 == 0)
            ]
            neighbors = [(x, y) for x, y in neighbors if x >= 0 and x < self.w and y >= 0 and y < self.h]
            for x, y in neighbors:
                self.nums[y][x] += 1
                if self.nums[y][x] > 9:
                    flashers.add((x, y))

    def reset(self):
        for x, y in [(i, j) for i in range(self.w) for j in range(self.h)]:
            if self.nums[y][x] > 9:
                self.nums[y][x] = 0
            self.flashed = [[False for _ in range(self.w)] for _ in range(self.h)]

    def first_sync_flash(self):
        i = 0
        done = False
        while not done:
            pre = self.count
            self.tick()
            done = (self.count - pre) == (self.w * self.h)
            i += 1
        return i


if __name__ == "__main__":
    with open("input.txt") as f:
        nums = [[int(c) for c in ln.strip()] for ln in f.readlines()]

    # part one
    g = Grid(nums)
    for _ in range(100):
        g.tick()
    print(g.count)

    # part two
    g = Grid(nums)
    print(f"Synchronized on step {g.first_sync_flash()}")
