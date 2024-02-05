import unittest
from unittest.mock import patch
from io import StringIO

# Import our program
from your_solution import Solution

class TestTopFour(unittest.TestCase):
    def test_main(self):
        test_class = Solution()
        answer = test_class.returnTopFour()
        expected_out = [['Brentford', 73, 60, 108], ['Brighton', 62, 47, 104], ['Man City', 59, 39, 87], ['Everton', 61, 41, 100]]
        # Check stdout
        self.assertEqual(answer, expected_out)

if __name__ == '__main__':
    unittest.main()
