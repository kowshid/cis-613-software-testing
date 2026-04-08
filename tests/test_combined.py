import unittest
from src.triangle import triangle_identifier

INVALID = -1
SCALENE = 0
ISOSCELES = 1
EQUILATERAL = 2

POSITIVE_SIDE_LENGTH = 10
MIN_SIDE_LENGTH = 1
MAX_SIDE_LENGTH = 200


class TestTriangleCombinedMutation(unittest.TestCase):

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

    def test_weak_normal_equivalence_class(self):
        self.assertEqual(triangle_identifier(5, 5, 5), EQUILATERAL)
        self.assertEqual(triangle_identifier(2, 2, 3), ISOSCELES)
        self.assertEqual(triangle_identifier(3, 4, 5), SCALENE)
        self.assertEqual(triangle_identifier(4, 1, 2), INVALID)

    # Rule 1: Any side out of bounds [1, 200] → INVALID
    def test_dt_rule_1_out_of_bounds(self):
        self.assertEqual(triangle_identifier(0, 5, 5), INVALID)
        self.assertEqual(triangle_identifier(201, 5, 5), INVALID)

    # Rule 2: Sides in bounds but fail triangle inequality → INVALID
    def test_dt_rule_2_fails_triangle_inequality(self):
        self.assertEqual(triangle_identifier(1, 2, 4), INVALID)
        self.assertEqual(triangle_identifier(4, 1, 2), INVALID)
        self.assertEqual(triangle_identifier(2, 4, 1), INVALID)

    # Rule 3: a == b == c → EQUILATERAL
    def test_dt_rule_3_equilateral(self):
        self.assertEqual(triangle_identifier(5, 5, 5), EQUILATERAL)

    # Rule 4: a == b, b != c → ISOSCELES
    def test_dt_rule_4_isosceles_ab(self):
        self.assertEqual(triangle_identifier(5, 5, 3), ISOSCELES)

    # Rule 5: b == c, a != b → ISOSCELES
    def test_dt_rule_5_isosceles_bc(self):
        self.assertEqual(triangle_identifier(3, 5, 5), ISOSCELES)

    # Rule 6: a == c, a != b → ISOSCELES
    def test_dt_rule_6_isosceles_ac(self):
        self.assertEqual(triangle_identifier(5, 3, 5), ISOSCELES)

    # Rule 7: a != b, b != c, a != c → SCALENE
    def test_dt_rule_7_scalene(self):
        self.assertEqual(triangle_identifier(3, 4, 5), SCALENE)


if __name__ == "__main__":
    unittest.main()
