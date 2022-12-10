import unittest
# Change the day imprt, day number and expected results
from advent2022 import day9 as puzzle
DAY = 9
RESULT_PART_1 = 13
RESULT_PART_2 = 1
#######################


class TestDaay(unittest.TestCase):
    def test_part1(self):
        if RESULT_PART_1 is None:
            self.skipTest("No result for part 1")
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part2(self):
        if RESULT_PART_2 is None:
            self.skipTest("No result for part 2")
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_2(data), RESULT_PART_2)

    def test_new_pos(self):
        self.assertEqual(puzzle.new_pos([4, 1], [4, 0]), [4, 0])
        self.assertEqual(puzzle.new_pos([2, 3], [3, 4]), [3, 4])
