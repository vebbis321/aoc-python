sum = 0

with open("./input.txt", "r") as f:
    for idx, line in enumerate(f):
        dict = {"green": 0, "blue": 0, "red": 0}
        cubes = line.removeprefix(f"Game {idx + 1}:")
        sets = [cube for cube in cubes.split(";")]
        for s in sets:
            splitted = s.split(",")
            for val in splitted:
                v, k = val.split()

                if dict[k] < int(v):
                    dict[k] = int(v)

        if dict["red"] <= 12 and dict["green"] <= 13 and dict["blue"] <= 14:
            game = idx + 1
            print(game)
            sum += game
    print(sum)
