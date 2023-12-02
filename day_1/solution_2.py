import re

sum = 0

str_nums = {
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
}


def transform_str_num_to_str_digit(num_str: str):
    match num_str:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"


with open("./input_2.txt", "r") as f:
    for line in f:
        numbers_in_line = []
        current_word = ""
        numbers_in_line = re.findall(r"(?=(" + "|".join(str_nums) + r"))", line)

        for idx, str_num in enumerate(numbers_in_line):
            if len(str_num) != 1:
                numbers_in_line[idx] = transform_str_num_to_str_digit(str_num)

        number = numbers_in_line[0] + numbers_in_line[-1]
        print(sum, number, numbers_in_line, line)
        sum += int(number)

    print(sum)
