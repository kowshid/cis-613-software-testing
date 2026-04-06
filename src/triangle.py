INVALID = -1
SCALENE = 0
ISOSCELES = 1
EQUILATERAL = 2


def triangle_identifier(a, b, c):

    is_a_triangle = None

    if not (1 <= a <= 200) or not (1 <= b <= 200) or not (1 <= c <= 200):
        is_a_triangle = False
    elif (a < b + c) and (b < a + c) and (c < a + b):
        is_a_triangle = True
    else:
        is_a_triangle = False

    triangle_type = INVALID
    if is_a_triangle:
        if (a == b) and (b == c):
            triangle_type = EQUILATERAL
        elif (a != b) and (a != c) and (b != c):
            triangle_type = SCALENE
        else:
            triangle_type = ISOSCELES
    else:
        triangle_type = INVALID

    return triangle_type