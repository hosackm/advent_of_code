def count_ones(lines):
    n = len(lines[0])
    counts = [0] * n

    for num in lines:
        for i, b in enumerate(num):
            if b == "1":
                counts[i] += 1

    gamma, epsilon = 0, 0
    half = len(lines) // 2
    for i, c in enumerate(counts):
        if c > half:
            gamma += 1 << (n - 1 - i)
        else:
            epsilon += 1 << (n - 1 - i)

    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")
    print(f"product: {gamma*epsilon}")

    return counts


def measure_oxygen(lines, counts):
    half = len(lines)//2
    for i, c in enumerate(counts):
        j = 0
        while j < len(lines) and len(lines) > 1:
            if c > half:
                if lines[j][i] == "0":
                    lines.pop(j)
                    continue
                else:
                    j += 1
            else:
                if lines[j][i] == "1":
                    lines.pop(j)
                    continue
                else:
                    j += 1

    return lines


def measure_scrubber(lines, counts):
    half = len(lines)//2
    for i, c in enumerate(counts):
        j = 0
        while j < len(lines) and len(lines) > 1:
            if c < half:
                if lines[j][i] == "0":
                    lines.pop(j)
                    continue
                else:
                    j += 1
            else:
                if lines[j][i] == "1":
                    lines.pop(j)
                    continue
                else:
                    j += 1

    return lines


if __name__ == "__main__":
    lines = []
    with open("../input.txt") as f:
        lines = [ln.strip() for ln in f.readlines()]

    counts = count_ones(lines)
    oxy = measure_oxygen(lines, counts)
    scrub = measure_scrubber(lines, counts)
    print(oxy, scrub)
