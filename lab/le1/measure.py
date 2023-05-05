"""
ALEJANDRE JOSE R. SAN PEDRO
LAB 1
"""


INCHES_CHOICE = "inches"
CM_CHOICE = "cm"

CONVERSION_FACTOR = 2.54


old_unit = input(f"Unit of measurement [\"{INCHES_CHOICE}\" or \"{CM_CHOICE}\"]: ")
new_unit = ""

old_value = float(input("Measurement value [float]: "))
new_value = 0.0


if old_unit == INCHES_CHOICE:
    new_unit = CM_CHOICE

    new_value = old_value * CONVERSION_FACTOR
elif old_unit == CM_CHOICE:
    new_unit = INCHES_CHOICE
    
    new_value = old_value / CONVERSION_FACTOR

new_value = round(new_value, 2)


print()
print(f"{old_value} {old_unit} is {new_value} {new_unit}")
