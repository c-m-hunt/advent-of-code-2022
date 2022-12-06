import unittest
import day6


class TestDay6(unittest.TestCase):
    def test_part1(self):
        data = day6.load_and_parse_data(6, True)
        self.assertEqual(day6.solve_part_1(data), 7)

    def test_part2(self):
        data = day6.load_and_parse_data(6, True)
        self.assertEqual(day6.solve_part_2(data), 19)
