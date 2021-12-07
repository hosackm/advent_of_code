from collections import Counter
from dataclasses import dataclass


@dataclass
class Answer:
    position: int
    cost: int


def nth_triangle_number(n):
    return ((n**2)+n)//2


def calculate_least_fuel(nums):
    counter = Counter(nums)
    min_bound, max_bound = min(counter.keys()), max(counter.keys())

    # key is the horizontal position, value is the fuel cost to move there
    fuel_costs = {}
    for target_x in range(min_bound, max_bound+1):
        count = 0
        for start_x, num_crabs in counter.items():
            # part one:
            # fuel_cost = abs(target_x - start_x)
            # part two:
            fuel_cost = nth_triangle_number(abs(target_x - start_x))
            count += fuel_cost * num_crabs
        fuel_costs[target_x] = count

    min_cost = None
    x_min_cost = -1
    for pos_x, cost in fuel_costs.items():
        if min_cost is None or cost < min_cost:
            min_cost = cost
            x_min_cost = pos_x

    return Answer(x_min_cost, min_cost)


if __name__ == "__main__":
    with open("input.txt") as f:
        nums = [int(n) for n in f.read().split(",")]

    answer = calculate_least_fuel(nums)
    print(answer)
