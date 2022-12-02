import math

filename = "./input/1.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

elf_no = 0
elf_calories = {elf_no: 0}
for line in lines:
    if line == "":
        elf_no += 1
        elf_calories[elf_no] = 0
        continue
    calories = int(line)
    elf_calories[elf_no] += calories

print("Part 1:", max(elf_calories.values()))

calorie_values = [value for value in elf_calories.values()]
calorie_values.sort(reverse=True)

print("Part 2:", sum(calorie_values[0:3]))
