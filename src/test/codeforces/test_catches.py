import unittest
from src.main.codeforces.catches import *

class TestCatches(unittest.TestCase):

    # @unittest.skip
    # def test_get_time(self):
    #     self.assertEqual(get_time(1, [(2, 5, 2)], 10), 18)
    #     self.assertEqual(get_time(1, [(2, 5, 2), (4, 7, 2)], 10), 22)
    #     self.assertEqual(get_time(1, [(2, 5, 2), (6, 8, 2)], 10), 24)

    # def test_search(self):
    #     # print(get_time(1, [(2, 5, 2)], 10))
    #     self.assertEqual(search([(2, 5, 2)], 10, 18, 0, 100), 1)
    #     self.assertEqual(search([(2, 5, 2), (4, 7, 2)], 10, 22, 0, 100), 1)
    #     self.assertEqual(search([(2, 5, 2), (6, 8, 2)], 10, 24, 0, 100), 1)

    # def test_solve1(self):
    #     cs = [(2, 5, 2), (6, 8, 2), (7, 7, 1)]
    #     time = 24
    #     goal = 10
    #     solgers = [0, 0, 1, 1, 2, 2]
    #     self.assertEqual(solve(cs, goal, solgers, time), 2)

    def test_solve2(self):
        cs = [
            (1, 5, 2),
            (1, 2, 5),
            (2, 3, 5),
            (3, 5, 3)
        ]
        # 5 6 4 14
        time = 14
        goal = 6
        solgers = [1, 2, 3, 4, 5]
        print(solve(cs, goal, solgers, time))
        # self.assertEqual(solve(cs, goal, solgers, time), 2)

