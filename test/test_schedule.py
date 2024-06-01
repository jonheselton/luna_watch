import unittest
from code.schedule import *

class TestSchedule(unittest.TestCase):
    def test_init(self):
        a = Schedule()
        self.assertIsInstance(a, Schedule)


if __name__ == '__main__':
    unittest.main()