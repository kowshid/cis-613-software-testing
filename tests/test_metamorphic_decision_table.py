import unittest
from src.triangle import triangle_identifier, EQUILATERAL, SCALENE, ISOSCELES, INVALID

INTEGER_MULTIPLIER = 3
FLOAT_MULTIPLIER = 0.5


class TestTriangleDecisionTable(unittest.TestCase):

    # Rule 1: Any side non-positive → INVALID
    def test_dt_rule_1_out_of_bounds(self):
        self.assertEqual(triangle_identifier(0, 5, 5), INVALID)
        self.assertEqual(triangle_identifier(-1, 5, 5), INVALID)

        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 0, INTEGER_MULTIPLIER * 5, INTEGER_MULTIPLIER * 5),
                         INVALID)
        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * -1, INTEGER_MULTIPLIER * 5, INTEGER_MULTIPLIER * 5),
                         INVALID)

        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 0, FLOAT_MULTIPLIER * 5, FLOAT_MULTIPLIER * 5), INVALID)
        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * -1, FLOAT_MULTIPLIER * 5, FLOAT_MULTIPLIER * 5),
                         INVALID)

    # Rule 2: Sides in bounds but fail triangle inequality → INVALID
    def test_dt_rule_2_fails_triangle_inequality(self):
        self.assertEqual(triangle_identifier(1, 2, 4), INVALID)
        self.assertEqual(triangle_identifier(4, 1, 2), INVALID)
        self.assertEqual(triangle_identifier(2, 4, 1), INVALID)

        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 1, INTEGER_MULTIPLIER * 2, INTEGER_MULTIPLIER * 4),
                         INVALID)
        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 4, INTEGER_MULTIPLIER * 1, INTEGER_MULTIPLIER * 2),
                         INVALID)
        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 2, INTEGER_MULTIPLIER * 4, INTEGER_MULTIPLIER * 1),
                         INVALID)

        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 1, FLOAT_MULTIPLIER * 2, FLOAT_MULTIPLIER * 4), INVALID)
        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 4, FLOAT_MULTIPLIER * 1, FLOAT_MULTIPLIER * 2), INVALID)
        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 2, FLOAT_MULTIPLIER * 4, FLOAT_MULTIPLIER * 1), INVALID)

    # Rule 3: a == b == c → EQUILATERAL
    def test_dt_rule_3_equilateral(self):
        self.assertEqual(triangle_identifier(5, 5, 5), EQUILATERAL)

        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 5, INTEGER_MULTIPLIER * 5, INTEGER_MULTIPLIER * 5),
                         EQUILATERAL)

        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 5, FLOAT_MULTIPLIER * 5, FLOAT_MULTIPLIER * 5),
                         EQUILATERAL)

    # Rule 4: a == b, b != c → ISOSCELES
    def test_dt_rule_4_isosceles_ab(self):
        self.assertEqual(triangle_identifier(5, 5, 3), ISOSCELES)

        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 5, INTEGER_MULTIPLIER * 5, INTEGER_MULTIPLIER * 3),
                         ISOSCELES)

        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 5, FLOAT_MULTIPLIER * 5, FLOAT_MULTIPLIER * 3),
                         ISOSCELES)

    # Rule 5: b == c, a != b → ISOSCELES
    def test_dt_rule_5_isosceles_bc(self):
        self.assertEqual(triangle_identifier(3, 5, 5), ISOSCELES)

        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 3, INTEGER_MULTIPLIER * 5, INTEGER_MULTIPLIER * 5),
                         ISOSCELES)

        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 3, FLOAT_MULTIPLIER * 5, FLOAT_MULTIPLIER * 5),
                         ISOSCELES)

    # Rule 6: a == c, a != b → ISOSCELES
    def test_dt_rule_6_isosceles_ac(self):
        self.assertEqual(triangle_identifier(5, 3, 5), ISOSCELES)

        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 5, INTEGER_MULTIPLIER * 3, INTEGER_MULTIPLIER * 5),
                         ISOSCELES)

        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 5, FLOAT_MULTIPLIER * 3, FLOAT_MULTIPLIER * 5),
                         ISOSCELES)

    # Rule 7: a != b, b != c, a != c → SCALENE
    def test_dt_rule_7_scalene(self):
        self.assertEqual(triangle_identifier(3, 4, 5), SCALENE)

        self.assertEqual(triangle_identifier(INTEGER_MULTIPLIER * 3, INTEGER_MULTIPLIER * 4, INTEGER_MULTIPLIER * 5),
                         SCALENE)

        self.assertEqual(triangle_identifier(FLOAT_MULTIPLIER * 3, FLOAT_MULTIPLIER * 4, FLOAT_MULTIPLIER * 5), SCALENE)


if __name__ == "__main__":
    unittest.main()
