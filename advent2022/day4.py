from typing import List
from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    lines = utils.get_input(day, test)
    return [line.rstrip().split(",") for line in lines]


def solve_part_1(data):
    full_intersect = 0
    for p in data:
        e1 = get_range(p[0])
        e2 = get_range(p[1])
        if len(set(e1).intersection(set(e2))) == len(set(e1)) or len(set(e2).intersection(set(e1))) == len(set(e2)):
            full_intersect += 1
    return full_intersect


def solve_part_2(data):
    part_intersect = 0
    for p in data:
        e1 = get_range(p[0])
        e2 = get_range(p[1])
        if len(set(e1).intersection(set(e2))) > 0:
            part_intersect += 1
    return part_intersect


def get_range(ranges: List[str]) -> List[int]:
    start = int(ranges.split("-")[0])
    end = int(ranges.split("-")[1])
    return list(range(start, end + 1))
