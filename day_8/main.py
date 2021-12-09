from collections import defaultdict


class Display:
    s_to_n = {              # 7-segment-display
                            # sections
        "abcefg": 0,        #   aaaa
        "cf": 1,            #  b    c
        "acdeg": 2,         #  b    c
        "acdfg": 3,         #   dddd
        "bcdf": 4,          #  e    f
        "abdfg": 5,         #  e    f
        "abdefg": 6,        #   gggg
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    @classmethod
    def to_number(cls, s):
        s = "".join(sorted(s))
        return cls.s_to_n[s]

    @classmethod
    def to_segments(cls, n):
        return {v: k for k, v in cls.s_to_n.items()}[n]


class WiringDecoder:
    def __init__(self, signals):
        self.mapping = {}
        self.len_table = defaultdict(list)
        for s in signals:
            self.len_table[len(s)].append(s)
        self.solve()

    def decode(self, s):
        out = ""
        for c in s:
            for k, v in self.mapping.items():
                if v == c:
                    out += k
                    continue
        return out

    def decode_n(self, nums):
        return [self.decode(n) for n in nums]

    def solve(self):
        self.find_a()
        self.find_e_and_g()
        self.find_b_and_d()
        self.find_c_and_f()

    def get_four_segments(self):
        return self.len_table[4][0]

    def get_one_segments(self):
        return self.len_table[2][0]

    def get_seven_segments(self):
        return self.len_table[3][0]

    def get_eight_segements(self):
        return self.len_table[7][0]

    def get_six_part_segments(self):
        return self.len_table[6]

    def find_a(self):
        a = set(self.get_seven_segments()) - set(self.get_one_segments())
        self.mapping["a"] = a.pop()

    def find_e_and_g(self):
        """e and g can be isolated by finding the difference between an 8 and a 4 on the
        display. We don't know which is e and which is g so we compare to the six segment
        9, 6, 0.  The e is missing in the 9 so it will only appear in 2
        of the 3 six-segment numbers (ie. 6, 0).  So, we can deduce which is e and g.
        """
        eg = set(self.get_eight_segements()) - set(self.get_four_segments())
        eg = eg - set(self.mapping["a"])
        six_segs = self.get_six_part_segments()

        for c in eg:
            count = sum(c in n for n in six_segs)
            if count == 2:
                self.mapping["e"] = c
            else:
                self.mapping["g"] = c

    def find_b_and_d(self):
        """b and d can be isolated by finding the difference between an 4 and a 1 on the
        display. We don't know which is b and which is d so we compare to the six segment
        9, 6, 0.  The d is missing in the 0 so it will only appear in 2
        of the 3 six-segment numbers (ie. 6, 9).  So, we can deduce which is b and d.
        """
        bd = list(set(self.get_four_segments()) - set(self.get_one_segments()))
        six_segs = self.get_six_part_segments()
        if sum(bd[0] in n for n in six_segs) == 2:
            self.mapping["d"] = bd[0]
            self.mapping["b"] = bd[1]
        else:
            self.mapping["d"] = bd[1]
            self.mapping["b"] = bd[0]

    def find_c_and_f(self):
        """c and f can be isolated by finding 1 on the display. We don't know which is c
        and which is f so we compare to the six segment 9, 6, 0.  The c is missing in
        the 6 so it will only appear in 2
        of the 3 six-segment numbers (ie. 0, 9).  So, we can deduce which is c and f.
        """
        cf = self.get_one_segments()
        six_segs = self.get_six_part_segments()
        if sum(cf[0] in n for n in six_segs) == 2:
            self.mapping["c"] = cf[0]
            self.mapping["f"] = cf[1]
        else:
            self.mapping["c"] = cf[1]
            self.mapping["f"] = cf[0]


if __name__ == "__main__":
    signals = []
    output = []
    with open("input.txt") as f:
        for line in f.readlines():
            sig, out = line.split(" | ")
            signals.append(sig.split())
            output.append(out.split())

    # part one
    count = sum(1 if len(d) in [2, 3, 4, 7] else 0 for n in output for d in n)
    print(f"1, 4, 7, or 8 occurred {count} times")

    # part two
    all_results = []
    for sig, o in zip(signals, output):
        s = WiringDecoder(sig)
        dec = s.decode_n(o)
        nums = [Display.to_number(d) for d in dec]
        all_results.append(nums[0]*1000 + nums[1]*100 + nums[2]*10 + nums[3])

    print(sum(all_results))
