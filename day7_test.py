import unittest
import day7 as puzzle

DAY = 7


class TestDay6(unittest.TestCase):
    def test_part1(self):
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_1(data), 95437)

    def test_part2(self):
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_2(data), 24933642)
