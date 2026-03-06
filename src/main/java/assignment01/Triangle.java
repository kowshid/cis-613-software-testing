package assignment01;

public class Triangle {

    public static final int INVALID = -1;
    public static final int SCALENE = 0;
    public static final int ISOSCELES = 1;
    public static final int EQUILATERAL = 2;

    public static int triangleIdentifier(int a, int b, int c) {

        boolean isATriangle;

        // Is A Triangle?
        if ((a < b + c) && (b < a + c) && (c < a + b))
            isATriangle = true;
        else
            isATriangle = false;

        // Determine Triangle Type
        int triangleType = INVALID;
        if (isATriangle) {
            if ((a == b) && (b == c))
                triangleType = EQUILATERAL;
            else if ((a != b) && (a != c) && (b != c))
                triangleType = SCALENE;
            else
                triangleType = ISOSCELES;
        } else
            triangleType = INVALID;

        return triangleType;
    }
}