import unittest
import importlib
# Change the day imprt, day number and expected results
DAY = 6
RESULT_PART_1 = 7
RESULT_PART_2 = 19
#######################
puzzle = importlib.import_module("advent2022.day" + str(DAY))


class TestDay6(unittest.TestCase):
    def test_part1(self):
        data = puzzle.load_and_parse_data(6, True)
        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part2(self):
        data = puzzle.load_and_parse_data(6, True)
        self.assertEqual(puzzle.solve_part_2(data), RESULT_PART_2)
