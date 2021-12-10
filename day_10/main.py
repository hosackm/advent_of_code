class IncompleteLineException(Exception):
    pass


class CorruptedLineException(Exception):
    pass


class Parser:
    def __init__(self):
        self.token_info = {
            "(": {"cost": 3, "completion": ")", "completion_cost": 1},
            "[": {"cost": 57, "completion": "]", "completion_cost": 2},
            "{": {"cost": 1197, "completion": "}", "completion_cost": 3},
            "<": {"cost": 25137, "completion": ">", "completion_cost": 4},
        }
        self.to_open = {")": "(", "}": "{", ">": "<", "]": "["}

        # per parse variables
        self.complete = ""
        self.count = 0

    def parse(self, input):
        self.count = 0
        self.complete = ""

        opened = []
        for token in input:
            if token in self.token_info:
                opened.append(token)
            else:
                op = opened.pop()
                info = self.token_info[op]
                if token != info["completion"]:
                    got_key = self.to_open[token]
                    self.count = self.token_info[got_key]["cost"]
                    raise CorruptedLineException

        if opened:
            self.complete = "".join(self.token_info[c]["completion"] for c in opened[::-1])
            raise IncompleteLineException

    def autocomplete_score(self):
        score = 0
        for c in self.complete:
            score *= 5
            score += self.token_info[self.to_open[c]]["completion_cost"]
        return score


def get_middle_sorted(scores):
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [ln.strip() for ln in f.readlines()]

    p = Parser()
    count = 0
    scores = []
    for ln in lines:
        try:
            p.parse(ln)
        except IncompleteLineException:
            scores.append(p.autocomplete_score())
        except CorruptedLineException:
            pass
        finally:
            count += p.count

    print(count)
    print(get_middle_sorted(scores))
