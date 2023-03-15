# INPUT SIDES
side1 = float(input())
side2 = float(input())
side3 = float(input())



# CHECK VALIDITY
valid = True

# check negatives
if ((side1 < 0) or (side2 < 0) or (side3 < 0)):
    valid = False

# check triangle inequality theorem
if ((side1 + side2 <= side3) or
    (side1 + side3 <= side2) or 
    (side2 + side3 <= side1)):
    
    valid = False


# CHECK EQUAL SIDES
equal_sides = 0

# count how many times equal sides were detected (1,2,3)
if side1 == side2:
    equal_sides += 1
if side1 == side3:
    equal_sides += 1
if side2 == side3:
    equal_sides += 1
    
# correct to actual equal sides count (0 -> 0, 1 -> 2, 2 -> 3)
if 1 <= equal_sides <= 2:
    equal_sides += 1



# OUTPUT TRIANGLE TYPE
if not valid:
    print("INVALID")
else:
    if equal_sides == 0:
        print("SCALENE TRIANGLE")
    elif equal_sides == 2:
        print("ISOSCELES TRIANGLE")
    elif equal_sides == 3:
        print("EQUILATERAL TRIANGLE")
        