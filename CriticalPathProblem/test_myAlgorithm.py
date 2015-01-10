from unittest import TestCase, TestLoader, TextTestRunner
from CriticalPathProblem.critical_path_problem import MyAlgorithm

__author__ = 'Tong'


class TestMyAlgorithm(TestCase):
    def setUp(self):
        self.graph = []
        self.solution = []

    def test_sample1(self):
        self.graph = {'v': [1, 4, 2, 3], 'e': [[1, 4], [4, 2], [2, 3], [1, 2]]}
        self.solution = [1, 4, 2, 3]

        self.assertEqual(MyAlgorithm().get_critical_path(self.graph), self.solution)

    def test_sample2(self):
        self.graph = {'v': [6, 3, 1, -4, 7], 'e': [[6, 3], [3, 1], [1, -4], [-4, 7], [6, 1], [1, 7], [3, -4], [3, 7]]}
        self.solution = [6, 3, 1, 7]

        self.assertEqual(MyAlgorithm().get_critical_path(self.graph), self.solution)

    def test_sample3(self):
        self.graph = {'v': [10, 5, -1, 4, 2], 'e': [[10, 5], [5, -1], [-1, 4], [10, 4], [5, 2], [-1, 2]]}
        self.solution = [10, 5, -1, 4]

        self.assertEqual(MyAlgorithm().get_critical_path(self.graph), self.solution)


suite = TestLoader().loadTestsFromTestCase(TestMyAlgorithm)
TextTestRunner(verbosity=2).run(suite)