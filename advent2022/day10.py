from typing import List
import numpy as np
from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return [l.split(" ") for l in data]


def get_strengths(data):
    strengths = [1]
    for instruction in data:
        prev_strength = strengths[-1]
        if len(instruction) == 1:
            strengths.append(prev_strength)
            continue
        if instruction[0] == "addx":
            amount = int(instruction[1])
            strengths.append(prev_strength)
            strengths.append(prev_strength + amount)
    return strengths


def solve_part_1(data):
    sum_strengths = [20, 60, 100, 140, 180, 220]
    strengths = get_strengths(data)
    return sum([idx * strengths[idx - 1] for idx in sum_strengths])


def solve_part_2(data):
    strengths = get_strengths(data)
    display = np.zeros(6 * 40)
    for i, s in enumerate(strengths):
        j = i % 40
        if j - 1 <= s <= j + 1:
            display[i] = 1
    display = display.reshape(6, 40)
    for row in range(display.shape[0]):
        print("".join(["X" if int(display[row, col]) ==
              1 else " " for col in range(display.shape[1])]))
