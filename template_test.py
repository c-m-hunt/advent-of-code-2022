import unittest
import day7 as puzzle

DAY = None
RESULT_PART_1 = None
RESULT_PART_2 = None


class TestDaay(unittest.TestCase):
    def test_part1(self):
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part2(self):
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_2(data), RESULT_PART_2)
