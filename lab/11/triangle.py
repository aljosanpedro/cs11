from math import acos, pi


TRIANGLE_SIDES = 3
RADIANS_TO_DEGREES = 180/pi
RIGHT_ANGLE = 90


def main():
    # Input Sides
    sides = input_sides()
    
    # Not a Triangle
    is_triangle = check_triangle(sides)
    
    if not is_triangle:
        print("The sides don't form a triangle")
        return
    
    # Not a Right Triangle
    (angles, is_right_triangle) = check_right_triangle(sides)
    
    if not is_right_triangle:
        print(angles)
        return

    # Right Triangle
    print("Right Triangle!")


def input_sides():
    sides = []
    
    for _ in range(TRIANGLE_SIDES):
        side = float(input())        
        sides.append(side)
        
    return sides
    
        
def check_triangle(sides):
    (a, b, c) = sides
    
    if not ((a + b > c) and
            (a + c > b) and 
            (b + c > a)):
        return False

    return True


def check_right_triangle(sides):
    angles = []
    is_right_triangle = False
    
    
    # Cosines
    (a, b, c) = sides
    
    cos_a = (pow(b,2) + pow(c,2) - pow(a,2)) / (2 * b * c)
    cos_b = (pow(c,2) + pow(a,2) - pow(b,2)) / (2 * c * a)
    cos_c = (pow(a,2) + pow(b,2) - pow(c,2)) / (2 * a * b)
    # cos_c = 180 - cos_a - cos_b # alternative to previous line
    
    # Angles
    for cosine in (cos_a, cos_b, cos_c):
        angle = acos(cosine)
        angle *= RADIANS_TO_DEGREES
        angle = round(angle,2)
        
        angles.append(angle)
        
    angles.sort()
    
    """
    # Double-check if Triangle
    total_angle = 0
    
    for angle in angles:
        total_angle += angle
        
    if not total_angle == 180:
        print("Caught: not a triangle!")
        print("Passed triangle sides test but not angles test")
        return
    """
        
    # Check if Right Triangle
    for angle in angles:
        if angle == RIGHT_ANGLE:
            is_right_triangle = True
    
    
    return (angles, is_right_triangle)


main()
