package assignment01;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TriangleTest {

    public static final int POSITIVE_SIDE_LENGTH = 10;
    public static final int NEGATIVE_SIDE_LENGTH = -10;
    public static final int ZERO_SIDE_LENGTH = 0;

    @Test
    public void doesEqualSidesReturnAEquilateralTriangle() {
        assertEquals(Triangle.EQUILATERAL, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
    }

    @Test
    public void doesUnequalSidesReturnAScaleneTriangle() {
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH + 1));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH - 1));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH + 1));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1));
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH + 1, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH));
    }

    @Test
    public void doesTwoEqualSidesReturnAIsoscelesTriangle() {
        assertEquals(Triangle.ISOSCELES, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1));
        assertEquals(Triangle.ISOSCELES, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.ISOSCELES, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH - 1, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
    }

    @Test
    public void doesAllNegativeSidesReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH));
    }

    @Test
    public void doesTwoNegativeSidesReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH));
    }

    @Test
    public void doesOneNegativeSideReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, NEGATIVE_SIDE_LENGTH));

    }

    @Test
    public void doesAllZeroSidesReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH));
    }

    @Test
    public void doesTwoZeroSidesReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH, ZERO_SIDE_LENGTH));
    }

    @Test
    public void doesOneZeroSideReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH, ZERO_SIDE_LENGTH));
    }

    @Test
    public void doesOneBigSideReturnAnInvalidTriangle() {
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH, POSITIVE_SIDE_LENGTH));
        assertEquals(Triangle.INVALID, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH * 2, POSITIVE_SIDE_LENGTH));
    }

    @Test
    public void isValidTriangleBoundaryValueCovered() {
        assertEquals(Triangle.SCALENE, Triangle.triangleIdentifier(POSITIVE_SIDE_LENGTH * 3, POSITIVE_SIDE_LENGTH * 2, POSITIVE_SIDE_LENGTH + 1));
    }

    @Test
    void isValidIntegerBoundaryValueCovered() {
        assertEquals(Triangle.EQUILATERAL, Triangle.triangleIdentifier(Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MAX_VALUE));
        assertEquals(Triangle.ISOSCELES, Triangle.triangleIdentifier(Integer.MAX_VALUE, Integer.MAX_VALUE, 1));
    }
}