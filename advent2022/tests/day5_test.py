import unittest
import importlib
# Change the day imprt, day number and expected results
DAY = 5
RESULT_PART_1 = "CMZ"
RESULT_PART_2 = "MCD"
#######################
puzzle = importlib.import_module("advent2022.day" + str(DAY))


class TestDay5(unittest.TestCase):
    def test_part1(self):
        data = puzzle.load_and_parse_data(5, True)
        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part2(self):
        data = puzzle.load_and_parse_data(5, True)
        self.assertEqual(puzzle.solve_part_2(data), RESULT_PART_2)
