sum = 0

with open("./input.txt", "r") as f:
    for line in f:
        numbers_in_line = [s for s in line if s.isdigit()]
        first_and_last_num = numbers_in_line[0] + numbers_in_line[-1]

        sum += int(first_and_last_num)

    print(sum)
