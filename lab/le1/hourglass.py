"""
ALEJANDRE JOSE R. SAN PEDRO
LAB 1
"""

CIRCLE = 'o'
SPACE = ' '
DOT = '.'


height = int(input("Hourglass height [int]: "))
print()


base = 1

for _ in range(height-1):
    base += 2

half = int(base / 2)

# top base
print(CIRCLE * base)

# top half
outer_spaces = 0
inner_spaces = base - 2

for _ in range(half - 1):
    
    outer_spaces += 1
    inner_spaces -= 2

    print(f"{SPACE * outer_spaces}{CIRCLE}{SPACE * inner_spaces}{CIRCLE}{SPACE * outer_spaces}")

# center
print(f"{SPACE * half}{CIRCLE}{SPACE * half}")

# bottom half
outer_spaces = half
inner_dots = -1

for _ in range(half - 1):
    
    outer_spaces -= 1
    inner_dots += 2

    print(f"{SPACE * outer_spaces}{CIRCLE}{DOT * inner_dots}{CIRCLE}{SPACE * outer_spaces}")

# bottom base
print(CIRCLE * base)

