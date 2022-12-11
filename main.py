import importlib
import sys

DAY = sys.argv[1]

puzzle = importlib.import_module("advent2022.day" + DAY)

if __name__ == "__main__":
    data = puzzle.load_and_parse_data(DAY)
    print("Part 1:", puzzle.solve_part_1(data))
    data = puzzle.load_and_parse_data(DAY)
    print("Part 2:", puzzle.solve_part_2(data))
