from typing import List


def get_input(day: int) -> List[str]:
    filename = f"./input/{day}.txt"
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
