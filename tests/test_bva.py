import unittest
from src.triangle import triangle_identifier, EQUILATERAL, SCALENE, ISOSCELES, INVALID

POSITIVE_SIDE_LENGTH = 10
MIN_SIDE_LENGTH = 1
MAX_SIDE_LENGTH = 200


class TestTriangleBVA(unittest.TestCase):

    def test_does_equal_sides_return_equilateral_triangle(self):
        self.assertEqual(
            triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH),
            EQUILATERAL
        )

    def test_does_unequal_sides_return_scalene_triangle(self):
        self.assertEqual(triangle_identifier(10, 9, 11), SCALENE)
        self.assertEqual(triangle_identifier(10, 11, 9), SCALENE)
        self.assertEqual(triangle_identifier(9, 10, 11), SCALENE)
        self.assertEqual(triangle_identifier(9, 11, 10), SCALENE)
        self.assertEqual(triangle_identifier(11, 10, 9), SCALENE)
        self.assertEqual(triangle_identifier(11, 9, 10), SCALENE)

    def test_does_two_equal_sides_return_isosceles_triangle(self):
        self.assertEqual(triangle_identifier(10, 10, 9), ISOSCELES)
        self.assertEqual(triangle_identifier(10, 9, 10), ISOSCELES)
        self.assertEqual(triangle_identifier(9, 10, 10), ISOSCELES)

    def test_does_all_negative_sides_return_invalid_triangle(self):
        self.assertEqual(triangle_identifier(-10, -10, -10), INVALID)

    def test_does_two_negative_sides_return_invalid_triangle(self):
        self.assertEqual(triangle_identifier(-10, -10, 10), INVALID)
        self.assertEqual(triangle_identifier(-10, 10, -10), INVALID)
        self.assertEqual(triangle_identifier(10, -10, -10), INVALID)

    def test_does_one_negative_side_return_invalid_triangle(self):
        self.assertEqual(triangle_identifier(-10, 10, 10), INVALID)
        self.assertEqual(triangle_identifier(10, -10, 10), INVALID)
        self.assertEqual(triangle_identifier(10, 10, -10), INVALID)

    def test_does_all_zero_sides_return_invalid_triangle(self):
        self.assertEqual(triangle_identifier(0, 0, 0), INVALID)

    def test_does_two_zero_sides_return_invalid_triangle(self):
        self.assertEqual(triangle_identifier(0, 0, 10), INVALID)
        self.assertEqual(triangle_identifier(0, 10, 0), INVALID)
        self.assertEqual(triangle_identifier(10, 0, 0), INVALID)

    def test_does_one_zero_side_return_invalid_triangle(self):
        self.assertEqual(triangle_identifier(0, 10, 10), INVALID)
        self.assertEqual(triangle_identifier(10, 0, 10), INVALID)
        self.assertEqual(triangle_identifier(10, 10, 0), INVALID)

    def test_does_one_big_side_return_invalid_triangle(self):
        self.assertEqual(triangle_identifier(30, 10, 10), INVALID)
        self.assertEqual(triangle_identifier(30, 20, 10), INVALID)

    def test_is_valid_triangle_boundary_value_covered(self):
        self.assertEqual(triangle_identifier(30, 20, 11), SCALENE)

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
