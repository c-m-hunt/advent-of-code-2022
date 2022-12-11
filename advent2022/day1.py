import math

from typing import List

from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return [line.rstrip() for line in data]


def get_elf_calories(data) -> dict:
    elf_no = 0
    elf_calories = {elf_no: 0}
    for line in data:
        if line == "":
            elf_no += 1
            elf_calories[elf_no] = 0
            continue
        calories = int(line)
        elf_calories[elf_no] += calories
    return elf_calories


def solve_part_1(lines):
    elf_calories = get_elf_calories(lines)
    return max(elf_calories.values())


def solve_part_2(data):
    elf_calories = get_elf_calories(data)
    calorie_values = [value for value in elf_calories.values()]
    calorie_values.sort(reverse=True)
    return sum(calorie_values[0:3])
