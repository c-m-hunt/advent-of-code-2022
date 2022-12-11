from typing import List

from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return [line.rstrip() for line in data]


priorities = {l: i + 1 for i, l in enumerate(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}


def solve_part_1(data):
    total = 0
    for bp in data:
        bp1, bp2 = bp[:len(bp) // 2], bp[len(bp) // 2:]
        intersect = set(bp1).intersection(set(bp2))
        total += priorities[list(intersect)[0]]

    return total


def solve_part_2(data):
    i, total = 0, 0
    while i < len(data):
        intersect1 = set(data[i]).intersection(set(data[i + 1]))
        intersect2 = intersect1.intersection(set(data[i + 2]))
        total += priorities[list(intersect2)[0]]
        i += 3

    return total
