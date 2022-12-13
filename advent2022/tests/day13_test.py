import unittest
import importlib
# Change the day imprt, day number and expected results
DAY = 13
RESULT_PART_1 = 13
RESULT_PART_2 = 140
#######################
puzzle = importlib.import_module("advent2022.day" + str(DAY))


class TestDay(unittest.TestCase):
    def test_part1(self):
        if RESULT_PART_1 is None:
            self.skipTest("No result for part 1")
        data = puzzle.load_and_parse_data(DAY, True)

        self.assertEqual(puzzle.compare_pair(
            [1, 1, 3, 1, 1], [1, 1, 5, 1, 1]), True)

        self.assertEqual(puzzle.compare_pair(
            [9], [[8, 7, 6]]), False)

        self.assertEqual(puzzle.compare_pair(
            [[1, [9, [0], [8, 3]], [9, 10, [5, 10], [7, 7, 1, 8], [7]], [
                [], [5, 0, 8], 2, 5]], [], [6, 0, 10], [0, 4, 10, [], [3, 2, 5]], []],
            [[10, 2, 4, 10], [[[]], [[1]], 9], []]
        ), True)

        self.assertEqual(puzzle.compare_pair(
            [[3, 5, 6, 8], [3], [[[7, 2, 7, 5, 9], [2, 7, 10, 4]], 1, 6],
                [7, [[5, 3, 2, 0, 0]], [9], 6]],
            [[[3, 2, 6, 6, 1], [0, 10], [7, []], 2, 2], [], []]
        ), True)

        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part2(self):
        if RESULT_PART_2 is None:
            self.skipTest("No result for part 2")
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_2(data), RESULT_PART_2)
