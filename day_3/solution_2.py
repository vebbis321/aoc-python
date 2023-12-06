import re
from collections import defaultdict

symbols = "*"

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

    num_with_symbol_dict = defaultdict(set)

    for line in num_dict:
        for x, val in num_dict[line].items():
            # left
            if x - 1 in symbol_dict[line]:
                num_with_symbol_dict[f"x: {x - 1}, y: {line}"].add(val)

            # right
            if x + len(str(val)) in symbol_dict[line]:
                num_with_symbol_dict[f"x: {x + len(str(val))}, y: {line}"].add(val)

            # top
            for i in range(x - 1, x + len(str(val)) + 1):
                if i in symbol_dict[line - 1]:
                    num_with_symbol_dict[f"x: {i}, y: {line - 1}"].add(val)

            # bottom
            for i in range(x - 1, x + len(str(val)) + 1):
                if i in symbol_dict[line + 1]:
                    num_with_symbol_dict[f"x: {i}, y: {line + 1}"].add(val)

    for k, num_set in num_with_symbol_dict.items():
        if len(num_set) > 1:
            gear_ratio = 1
            for num in num_set:
                gear_ratio *= num

            sum += gear_ratio
    print(sum)
