from typing import List

import utils

DAY = 7


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    return utils.get_input(day, test)


def solve_part_1(data):
    pass


def solve_part_2(data):
    pass


if __name__ == "__main__":
    data = load_and_parse_data(DAY)
    print("Part 1:", solve_part_1(data))
    print("Part 2:", solve_part_2(data))
