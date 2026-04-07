import unittest
from src.triangle import triangle_identifier, EQUILATERAL, SCALENE, ISOSCELES, INVALID


class TestTriangleEquivalenceClass(unittest.TestCase):

    def test_weak_normal_equivalence_class(self):
        self.assertEqual(triangle_identifier(5, 5, 5), EQUILATERAL)
        self.assertEqual(triangle_identifier(2, 2, 3), ISOSCELES)
        self.assertEqual(triangle_identifier(3, 4, 5), SCALENE)
        self.assertEqual(triangle_identifier(4, 1, 2), INVALID)

if __name__ == "__main__":
    unittest.main()
