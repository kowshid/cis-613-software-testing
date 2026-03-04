package assignment01;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class TriangleTest {

    private static final int POSITIVE_SIDE_LENGTH = 10;
    private static final int NEGATIVE_SIDE_LENGTH = -10;
    private static final int ZERO_SIDE_LENGTH = 0;

    @Test
    void doesEqualSidesReturnAEquilateralTriangle() {
        assertEquals(Triangle.EQUILATERAL, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
    }

    @Test
    void doesUnequalSidesReturnAScaleneTriangle() {
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH + 1));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH - 1));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH + 1));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH));
    }

    @Test
    void doesTwoEqualSidesReturnAIsoscelesTriangle() {
        assertEquals(Triangle.ISOSCELES, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1));
        assertEquals(Triangle.ISOSCELES, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.ISOSCELES, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
    }

    @Test
    void doesAllNegativeSidesReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH));
    }

    @Test
    void doesTwoNegativeSidesReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH));
    }

    @Test
    void doesOneNegativeSideReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH));

    }

    @Test
    void doesAllZeroSidesReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH));
    }

    @Test
    void doesTwoZeroSidesReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH));
    }

    @Test
    void doesOneZeroSideReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH));
    }

    @Test
    void doesOneBigSideReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH * 2, POSITIVE_SIDE_LENGTH));
    }

    @Test
    void isValidTriangleBoundaryValueCovered() {
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH * 2, POSITIVE_SIDE_LENGTH + 1));
    }

    @Test
    void isValidIntegerBoundaryValueCovered() {
        assertEquals(Triangle.EQUILATERAL, Triangle.triangleIdentifier(Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MAX_VALUE));
        assertEquals(Triangle.EQUILATERAL, Triangle.triangleIdentifier(Integer.MAX_VALUE, Integer.MAX_VALUE, 1));
    }
}