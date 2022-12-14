from typing import List

from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return [l for l in data[0]]


def solve_part_1(data: List[str]) -> int:
    return find_marker(data, 4)


def solve_part_2(data):
    return find_marker(data, 14)


def find_marker(data: List[str], marker_length: int) -> int:
    test = 0
    while True:
        unique = set(data[test: test + marker_length])
        if len(unique) == marker_length:
            return test + marker_length
        test += 1
