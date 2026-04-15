import unittest

from src.triangle import triangle_identifier

# Assuming the function is in the same file or imported
# from triangle_script import triangle_identifier, INVALID, SCALENE, ISOSCELES, EQUILATERAL

class TestTriangleIdentifier(unittest.TestCase):

    ## --- Valid Triangle Tests ---

    def test_equilateral(self):
        """Tests that three equal sides return EQUILATERAL."""
        self.assertEqual(triangle_identifier(5, 5, 5), 2)  # EQUILATERAL

    def test_isosceles(self):
        """Tests that two equal sides return ISOSCELES."""
        self.assertEqual(triangle_identifier(5, 5, 8), 1)  # a == b
        self.assertEqual(triangle_identifier(5, 8, 5), 1)  # a == c
        self.assertEqual(triangle_identifier(8, 5, 5), 1)  # b == c

    def test_scalene(self):
        """Tests that three different sides return SCALENE."""
        self.assertEqual(triangle_identifier(3, 4, 5), 0)  # SCALENE

    ## --- Invalid Triangle Tests ---

    def test_invalid_triangle_inequality(self):
        """Tests cases where the sum of two sides is not greater than the third."""
        self.assertEqual(triangle_identifier(1, 2, 3), -1) # Sum equals third side
        self.assertEqual(triangle_identifier(1, 2, 10), -1) # Sum less than third side

    def test_invalid_zeros(self):
        """Tests that sides of zero length are INVALID."""
        self.assertEqual(triangle_identifier(0, 0, 0), -1)
        self.assertEqual(triangle_identifier(0, 5, 5), -1)

    def test_invalid_negatives(self):
        """Tests that negative side lengths are INVALID."""
        self.assertEqual(triangle_identifier(-1, -1, -1), -1)
        self.assertEqual(triangle_identifier(5, 5, -2), -1)

if __name__ == '__main__':
    unittest.main()
