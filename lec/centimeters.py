FEET_TO_INCHES = 12
INCHES_TO_CM = 2.54

DECIMALS = 2


feet = int(input())
inches = int(input())


inches += (feet * FEET_TO_INCHES)

cm = inches * INCHES_TO_CM
cm = round(centimeters, DECIMALS)


print(f"Your height in centimeters is {cm} centimeters")
