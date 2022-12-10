from advent2022 import day5
import unittest


class TestDay5(unittest.TestCase):
    def test_part1(self):
        data = day5.load_and_parse_data(5, True)
        self.assertEqual(day5.solve_part_1(data), "CMZ")

    def test_part2(self):
        data = day5.load_and_parse_data(5, True)
        self.assertEqual(day5.solve_part_2(data), "MCD")
