import unittest
from unittest.mock import patch
from io import StringIO

# Import our program
from your_solution import Solution

class TestTopFour(unittest.TestCase):
    def test_main(self):
        test_class = Solution()
        answer = test_class.returnTopFour()
        expected_out = [['Brentford', 73, 33, 108], ['Aston Villa', 62, 16, 113], ['Man City', 59, -4, 87], ['Everton', 61, 6, 100]]
        self.assertEqual(answer, expected_out)

if __name__ == '__main__':
    unittest.main()
