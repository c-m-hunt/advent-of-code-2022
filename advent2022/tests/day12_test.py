import unittest
import importlib
# Change the day imprt, day number and expected results
DAY = 12
RESULT_PART_1 = 31
RESULT_PART_2 = None
#######################
puzzle = importlib.import_module("advent2022.day" + str(DAY))


class TestDay(unittest.TestCase):
    def test_part1(self):
        if RESULT_PART_1 is None:
            self.skipTest("No result for part 1")
        data = puzzle.load_and_parse_data(DAY, True)

        # self.assertTrue(puzzle.valid_move(data, (2, 4), (2, 5)))
#
        # self.assertEqual(puzzle.get_directions(data, (2, 4)), [])

        # self.assertFalse(puzzle.valid_move(data, (0, 1), (-1, 1)))

        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part_1_live(self):
        if RESULT_PART_1 is None:
            self.skipTest("No result for part 1")
        data = puzzle.load_and_parse_data(DAY, False)

        # dirs = puzzle.get_directions(data, (2, 5))
        # self.assertEqual(dirs["up"], 23)
        # self.assertEqual(dirs["down"], 21)

        # dirs = puzzle.get_directions(data, (1, 0))
        # self.assertEqual(dirs["up"], -1)
        # self.assertEqual(dirs["down"], 0)

        # dirs = puzzle.get_directions(data, (1, 1))
        # self.assertEqual(dirs["up"], 0)
        # self.assertEqual(dirs["down"], 2)
        # self.assertEqual(dirs["left"], 0)
        # self.assertEqual(dirs["right"], 2)

        # next_point = puzzle.get_available_points(data, (1, 0))
        # self.assertEqual(next_point, [(0, 0), (2, 0)])

        # next_point = puzzle.get_available_points(data, (2, 5))
        # self.assertEqual(next_point, (2, 4))

        # self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part2(self):
        if RESULT_PART_2 is None:
            self.skipTest("No result for part 2")
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_2(data), RESULT_PART_2)
