import unittest
from src.triangle import triangle_identifier, EQUILATERAL, SCALENE, ISOSCELES, INVALID

POSITIVE_SIDE_LENGTH = 10
NEGATIVE_SIDE_LENGTH = -10
ZERO_SIDE_LENGTH = 0
MIN_SIDE_LENGTH = 1
MAX_SIDE_LENGTH = 200


class TestTriangleIdentifier(unittest.TestCase):

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

    def test_does_above_max_side_return_invalid_triangle(self):
        self.assertEqual(triangle_identifier(201, 10, 10), INVALID)
        self.assertEqual(triangle_identifier(10, 201, 10), INVALID)
        self.assertEqual(triangle_identifier(10, 10, 201), INVALID)

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

    def test_weak_normal_equivalence_class(self):
        self.assertEqual(triangle_identifier(5, 5, 5), EQUILATERAL)
        self.assertEqual(triangle_identifier(2, 2, 3), ISOSCELES)
        self.assertEqual(triangle_identifier(3, 4, 5), SCALENE)
        self.assertEqual(triangle_identifier(4, 1, 2), INVALID)

    def test_weak_robust_lower_bound_single_violation(self):
        self.assertEqual(triangle_identifier(0, 5, 5), INVALID)
        self.assertEqual(triangle_identifier(5, 0, 5), INVALID)
        self.assertEqual(triangle_identifier(5, 5, 0), INVALID)

    def test_weak_robust_upper_bound_single_violation(self):
        self.assertEqual(triangle_identifier(201, 5, 5), INVALID)
        self.assertEqual(triangle_identifier(5, 201, 5), INVALID)
        self.assertEqual(triangle_identifier(5, 5, 201), INVALID)

    def test_dt_rule_1_out_of_bounds(self):
        self.assertEqual(triangle_identifier(0, 5, 5), INVALID)
        self.assertEqual(triangle_identifier(201, 5, 5), INVALID)

    def test_dt_rule_2_fails_triangle_inequality(self):
        self.assertEqual(triangle_identifier(1, 2, 4), INVALID)
        self.assertEqual(triangle_identifier(4, 1, 2), INVALID)
        self.assertEqual(triangle_identifier(2, 4, 1), INVALID)

    def test_dt_rule_3_equilateral(self):
        self.assertEqual(triangle_identifier(5, 5, 5), EQUILATERAL)

    def test_dt_rule_4_isosceles_ab(self):
        self.assertEqual(triangle_identifier(5, 5, 3), ISOSCELES)

    def test_dt_rule_5_isosceles_bc(self):
        self.assertEqual(triangle_identifier(3, 5, 5), ISOSCELES)

    def test_dt_rule_6_isosceles_ac(self):
        self.assertEqual(triangle_identifier(5, 3, 5), ISOSCELES)

    def test_dt_rule_7_scalene(self):
        self.assertEqual(triangle_identifier(3, 4, 5), SCALENE)


if __name__ == "__main__":
    unittest.main()