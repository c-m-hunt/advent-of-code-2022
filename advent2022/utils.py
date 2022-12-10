from typing import List


def get_input(day: int, test: bool) -> List[str]:
    if test:
        filename = f"./advent2022/input/{day}_test.txt"
    else:
        filename = f"./advent2022/input/{day}.txt"
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
