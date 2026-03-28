import pytest
from src.triangle import triangle_identifier, EQUILATERAL, SCALENE, ISOSCELES, INVALID

POSITIVE_SIDE_LENGTH = 10
NEGATIVE_SIDE_LENGTH = -10
ZERO_SIDE_LENGTH = 0
MIN_SIDE_LENGTH = 1
MAX_SIDE_LENGTH = 200


def test_does_equal_sides_return_equilateral_triangle():
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == EQUILATERAL


def test_does_unequal_sides_return_scalene_triangle():
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH + 1) == SCALENE
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH - 1) == SCALENE
    assert triangle_identifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH + 1) == SCALENE
    assert triangle_identifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH) == SCALENE
    assert triangle_identifier(POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1) == SCALENE
    assert triangle_identifier(POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH) == SCALENE


def test_does_two_equal_sides_return_isosceles_triangle():
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1) == ISOSCELES
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH) == ISOSCELES
    assert triangle_identifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == ISOSCELES


def test_does_all_negative_sides_return_invalid_triangle():
    assert triangle_identifier(NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH) == INVALID


def test_does_two_negative_sides_return_invalid_triangle():
    assert triangle_identifier(NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH) == INVALID


def test_does_one_negative_side_return_invalid_triangle():
    assert triangle_identifier(NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH) == INVALID


def test_does_all_zero_sides_return_invalid_triangle():
    assert triangle_identifier(ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH) == INVALID


def test_does_two_zero_sides_return_invalid_triangle():
    assert triangle_identifier(ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH) == INVALID


def test_does_one_zero_side_return_invalid_triangle():
    assert triangle_identifier(ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH) == INVALID


def test_does_one_big_side_return_invalid_triangle():
    assert triangle_identifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH * 2, POSITIVE_SIDE_LENGTH) == INVALID


def test_is_valid_triangle_boundary_value_covered():
    assert triangle_identifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH * 2, POSITIVE_SIDE_LENGTH + 1) == SCALENE


def test_is_valid_bounds_boundary_value_covered():
    assert triangle_identifier(MIN_SIDE_LENGTH, MIN_SIDE_LENGTH, MIN_SIDE_LENGTH) == EQUILATERAL
    assert triangle_identifier(MAX_SIDE_LENGTH, MAX_SIDE_LENGTH, MAX_SIDE_LENGTH) == EQUILATERAL
    assert triangle_identifier(MAX_SIDE_LENGTH, MAX_SIDE_LENGTH, MIN_SIDE_LENGTH) == ISOSCELES


def test_does_above_max_side_return_invalid_triangle():
    assert triangle_identifier(MAX_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, MAX_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH) == INVALID
    assert triangle_identifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, MAX_SIDE_LENGTH + 1) == INVALID


def test_normal_bva_a_varies():
    assert triangle_identifier(100, 100, 100) == EQUILATERAL
    assert triangle_identifier(MIN_SIDE_LENGTH, 100, 100) == ISOSCELES
    assert triangle_identifier(MIN_SIDE_LENGTH + 1, 100, 100) == ISOSCELES
    assert triangle_identifier(MAX_SIDE_LENGTH - 1, 100, 100) == ISOSCELES
    assert triangle_identifier(MAX_SIDE_LENGTH, 100, 100) == INVALID


def test_normal_bva_b_varies():
    assert triangle_identifier(100, 100, 100) == EQUILATERAL
    assert triangle_identifier(100, MIN_SIDE_LENGTH, 100) == ISOSCELES
    assert triangle_identifier(100, MIN_SIDE_LENGTH + 1, 100) == ISOSCELES
    assert triangle_identifier(100, MAX_SIDE_LENGTH - 1, 100) == ISOSCELES
    assert triangle_identifier(100, MAX_SIDE_LENGTH, 100) == INVALID


def test_normal_bva_c_varies():
    assert triangle_identifier(100, 100, 100) == EQUILATERAL
    assert triangle_identifier(100, 100, MIN_SIDE_LENGTH) == ISOSCELES
    assert triangle_identifier(100, 100, MIN_SIDE_LENGTH + 1) == ISOSCELES
    assert triangle_identifier(100, 100, MAX_SIDE_LENGTH - 1) == ISOSCELES
    assert triangle_identifier(100, 100, MAX_SIDE_LENGTH) == INVALID


def test_weak_normal_equivalence_class():
    assert triangle_identifier(5, 5, 5) == EQUILATERAL
    assert triangle_identifier(2, 2, 3) == ISOSCELES
    assert triangle_identifier(3, 4, 5) == SCALENE
    assert triangle_identifier(4, 1, 2) == INVALID


def test_weak_robust_lower_bound_single_violation():
    assert triangle_identifier(MIN_SIDE_LENGTH - 1, 5, 5) == INVALID
    assert triangle_identifier(5, MIN_SIDE_LENGTH - 1, 5) == INVALID
    assert triangle_identifier(5, 5, MIN_SIDE_LENGTH - 1) == INVALID


def test_weak_robust_upper_bound_single_violation():
    assert triangle_identifier(MAX_SIDE_LENGTH + 1, 5, 5) == INVALID
    assert triangle_identifier(5, MAX_SIDE_LENGTH + 1, 5) == INVALID
    assert triangle_identifier(5, 5, MAX_SIDE_LENGTH + 1) == INVALID


# "Rule","Test Case Description","a","b","c","Expected Output","Rationale"
# "R1","Out of bounds input",0,5,5,-1,"Fails C1 (a < 1). Function should exit early."
# "R2","Fails Triangle Inequality",1,2,4,-1,"Fails C2 (1 + 2 is not > 4)."
# "R3","All sides equal",5,5,5,2,"Passes C3, C4, C5."
# "R4","Isosceles (a and b equal)",5,5,3,1,"Passes C3, fails C4 & C5."
# "R5","Isosceles (b and c equal)",3,5,5,1,"Passes C4, fails C3 & C5."
# "R6","Isosceles (a and c equal)",5,3,5,1,"Passes C5, fails C3 & C4."
# "R7","No sides equal",3,4,5,0,"Fails C3, C4, C5."

def test_dt_rule_1_out_of_bounds():
    assert triangle_identifier(MIN_SIDE_LENGTH - 1, 5, 5) == INVALID
    assert triangle_identifier(MAX_SIDE_LENGTH + 1, 5, 5) == INVALID

def test_dt_rule_2_fails_triangle_inequality():
    assert triangle_identifier(1, 2, 4) == INVALID
    assert triangle_identifier(4, 1, 2) == INVALID
    assert triangle_identifier(2, 4, 1) == INVALID

def test_dt_rule_3_equilateral():
    assert triangle_identifier(5, 5, 5) == EQUILATERAL

def test_dt_rule_4_isosceles_ab():
    assert triangle_identifier(5, 5, 3) == ISOSCELES

def test_dt_rule_5_isosceles_bc():
    assert triangle_identifier(3, 5, 5) == ISOSCELES

def test_dt_rule_6_isosceles_ac():
    assert triangle_identifier(5, 3, 5) == ISOSCELES

def test_dt_rule_7_scalene():
    assert triangle_identifier(3, 4, 5) == SCALENE
