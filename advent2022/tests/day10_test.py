import unittest
from advent2022 import day10 as puzzle
DAY = 10
RESULT_PART_1 = 13140


class TestDaay(unittest.TestCase):
    def test_part1(self):
        if RESULT_PART_1 is None:
            self.skipTest("No result for part 1")
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)
