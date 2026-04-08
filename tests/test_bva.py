import unittest
from src.triangle import triangle_identifier, EQUILATERAL, SCALENE, ISOSCELES, INVALID

POSITIVE_SIDE_LENGTH = 10
MIN_SIDE_LENGTH = 1
MAX_SIDE_LENGTH = 200


class TestTriangleBVA(unittest.TestCase):

    def test_is_valid_bounds_boundary_value_covered(self):
        self.assertEqual(triangle_identifier(1, 1, 1), EQUILATERAL)
        self.assertEqual(triangle_identifier(200, 200, 200), EQUILATERAL)
        self.assertEqual(triangle_identifier(200, 200, 1), ISOSCELES)

    def test_normal_bva_a_varies(self):
        self.assertEqual(triangle_identifier(100, 100, 100), EQUILATERAL)
        self.assertEqual(triangle_identifier(1, 100, 100), ISOSCELES)
        self.assertEqual(triangle_identifier(2, 100, 100), ISOSCELES)
        self.assertEqual(triangle_identifier(199, 100, 100), ISOSCELES)
        self.assertEqual(triangle_identifier(200, 100, 100), INVALID)

    def test_normal_bva_b_varies(self):
        self.assertEqual(triangle_identifier(100, 100, 100), EQUILATERAL)
        self.assertEqual(triangle_identifier(100, 1, 100), ISOSCELES)
        self.assertEqual(triangle_identifier(100, 2, 100), ISOSCELES)
        self.assertEqual(triangle_identifier(100, 199, 100), ISOSCELES)
        self.assertEqual(triangle_identifier(100, 200, 100), INVALID)

    def test_normal_bva_c_varies(self):
        self.assertEqual(triangle_identifier(100, 100, 100), EQUILATERAL)
        self.assertEqual(triangle_identifier(100, 100, 1), ISOSCELES)
        self.assertEqual(triangle_identifier(100, 100, 2), ISOSCELES)
        self.assertEqual(triangle_identifier(100, 100, 199), ISOSCELES)
        self.assertEqual(triangle_identifier(100, 100, 200), INVALID)


if __name__ == "__main__":
    unittest.main()
