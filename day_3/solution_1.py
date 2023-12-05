import re
from collections import defaultdict

symbols = "=+?#*&%@!$-/"

with open("./input.txt", "r") as f:
    num_dict = defaultdict(dict)
    symbol_dict = defaultdict(dict)
    sum = 0

    for line_idx, line in enumerate(f):
        num_dict[line_idx] = {
            m.start(): int(m.group()) for m in re.finditer(r"\d+", line.rstrip())
        }

        for char_idx, char in enumerate(line.rstrip()):
            if char in symbols:
                symbol_dict[line_idx][char_idx] = char

    for line in num_dict:
        for x, val in num_dict[line].items():
            # left
            if x - 1 in symbol_dict[line]:
                sum += val

            # right
            if x + len(str(val)) in symbol_dict[line]:
                sum += val

            # top
            for i in range(x - 1, x + len(str(val)) + 1):
                if i in symbol_dict[line - 1]:
                    sum += val

            # bottom
            for i in range(x - 1, x + len(str(val)) + 1):
                if i in symbol_dict[line + 1]:
                    sum += val

    print(sum)
