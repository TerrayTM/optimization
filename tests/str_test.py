import sys
import numpy as np

sys.path.append("../optimization")
sys.path.append("../optimization/enums")

from main import LinearProgrammingModel
from unittest import TestCase, main
from objective import Objective

class TestStr(TestCase):
    def test_str(self):
        # Write test cases here
        # Try to test as many cases as possible
        # Here is a simple example test
        # To run the test see README.md
        A = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        b = np.array([6, 15, 24])
        c = np.array([100, 200, 300])
        z = 5
        expected = (
            "Max [100. 200. 300.]x + 5\n"
            "Subject To:\n"
            "\n"
            "[1.0 2.0 3.0]     =   [6.0 ]\n"
            "[4.0 5.0 6.0]x    =   [15.0]\n"
            "[7.0 8.0 9.0]     =   [24.0]\n"
        )
        
        p = LinearProgrammingModel(A, b, c, z)

        # This test case should fail because you forgot the brackets around 'b'
        # Once you got that this should pass
        self.assertEqual(str(p), expected, "Should output in correct string format.")
       
if __name__ == "__main__":
    main()
