import re
from collections import defaultdict

with open("./input.txt", "r") as f:
    points = 0
    d = defaultdict(int)
    for line_idx, line in enumerate(f):
        mathces = 0
        arr = re.split("[:|]", line.rstrip())
        two_dim_arr = [a.split() for a in arr]

        d[int(two_dim_arr[0][1])] += 1
        j = d[int(two_dim_arr[0][1])]

        while j > 0:
            mathces = 0
            for num in two_dim_arr[2]:
                if num in two_dim_arr[1]:
                    mathces += 1
                    d[line_idx + 1 + mathces] += 1

            j -= 1

    for val in d.values():
        points += val

    print(points)
