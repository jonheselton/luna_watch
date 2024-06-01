import unittest
from code.classes import *

class TestSchedule(unittest.TestCase):
    def test_init(self):
        a = Schedule()
        self.assertIsInstance(a, Schedule)

class TestVisits(unittest.TestCase):
    def test_init(self):
        a = Visit()
        self.assertIsInstance(a, Visit)
if __name__ == '__main__':
    unittest.main()
