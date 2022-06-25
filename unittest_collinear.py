import unittest
import convex_hull
import numpy as np

class TestConvex_Hull(unittest.TestCase):

    def test_collinear(self):
        self.assertEqual(convex_hull.collinear(0,0),"ATTENTION: collineals points")


if __name__ == "__main__":
    unittest.main()