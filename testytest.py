import numpy as np

PIPI = np.pi

foo_bar = 3
bar_foo = 2

yes = foo_bar * bar_foo


print(yes)
print(PIPI)


print(2**3)
print(5 / 3)  # returns a float
yeee = 4
yeee = 2
foo = 5 // 3
bar = 5 / 3
print(5 // 3)  # integer divison
balls = "blue"
print(f"{balls}", end=" balls")
print("deez", end="\n")

# input_yes = input("who is de boss")

# some_str = balls == "blue" ? "ternary works!" : "nope"
some_str = "ternary works" if balls != "blue" else 2  # this is weird
# why is it a union????
# dynimc type...
print(some_str)

deez_lizts = [[]]
deez_lizts.append([4, 5, 6])

print(deez_lizts)

deez_lizts.remove([])

print(deez_lizts)

deez_lizts.append([1, 2, 4])
deez_lizts.append([8.8, 6, 7])

print(deez_lizts)
deez_new_lists = deez_lizts[1:2]
# from index and including one and to and not including 2
print(deez_new_lists)

deez_list = [0, 1, 2, 3, 10, 5, 6, 7, 8, 9, 10]
deez_list = deez_list[::2]
print(deez_list)

deez_list = deez_list[::-1]  # reversing deez
print(deez_list)

deez_list = deez_list + deez_list
print(deez_list)

print(deez_list.index(2))  # what is the idx of the number 2 in the list
print(deez_list.index(10))

deez_tuple = (2, "hello", 3)
print(deez_tuple)

deez_second_tuple: tuple[int | str, ...] = (1, 2, 3, "balls")
print(deez_second_tuple)

# deez_second_tuple.append("a") # cant modify tuple

print(deez_second_tuple[-1])  # but can access it of course

a, b, c = (1, 2, 3)
deez1, *deez2, deez3 = (1, 2, 3, 4)  # deez2 is now a list of 2 and 3
a, b = b, a  # lol swaps are simple

deez_dict = {}

deez_dict["balls"] = "blue"
deez_dict[3] = 420  # damn dict are flexible
print(deez_dict.values())
print(deez_dict["balls"])

m = {"Yes": 2, **{"a": 2}}
print(m)

# print(deez_dict[4])  # error
print(deez_dict.get(4))  # no error, returns none

deez_dict.setdefault(4, 4)  # insert if key is not present. Sets 4 to 4
deez_dict[4] = "four"
print(deez_dict[4])

set_deez_set = set()
set_deez_set = {1, 2, 3, 4}
set_deez_set.add(56)
print(set_deez_set)

deez_other_set = {99.0, 77, 6, 56}
print(set_deez_set & deez_other_set)  # intersection, what is common
print(set_deez_set | deez_other_set)  # union
print(set_deez_set - deez_other_set)  # diff

if deez_other_set >= set_deez_set:
    print("deez_other_set is a superset of set_deez_set")
elif 2 == 2:
    print("okay")
else:
    print(False)


for num in [420, 22, 3]:
    print(num)

for val, i in enumerate(["yes", "yp"]):
    print(i, val)

for val in range(2, 10, 2):
    print(val)

i = 4
while i > 0:
    i -= 1
    print(i)

try:
    raise IndexError("index get rekt")
finally:
    print("get rekt errors")
