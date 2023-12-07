import re

with open("./input.txt", "r") as f:
    points = 0

    for line_idx, line in enumerate(f):
        mathces = 0
        arr = re.split("[:|]", line.rstrip())
        two_dim_arr = [a.split() for a in arr]

        for num_idx, num in enumerate(two_dim_arr[2]):
            if num in two_dim_arr[1]:
                if mathces == 0:
                    mathces += 1
                else:
                    mathces *= 2

        points += mathces

    print(points)
