import unittest
# Change the day imprt, day number and expected results
from advent2022 import day11 as puzzle
DAY = 11
RESULT_PART_1 = 10605
RESULT_PART_2 = 2713310158
#######################


class TestDay(unittest.TestCase):
    def test_part1(self):
        if RESULT_PART_1 is None:
            self.skipTest("No result for part 1")
        data = puzzle.load_and_parse_data(DAY, True)
        monkey0 = data[0]
        self.assertEqual(monkey0.index, 0)
        self.assertEqual(monkey0.if_true, 2)
        self.assertEqual(monkey0.items, [79, 98])
        self.assertEqual(monkey0.if_false, 3)

        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part2(self):
        if RESULT_PART_2 is None:
            self.skipTest("No result for part 2")
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_2(data), RESULT_PART_2)
