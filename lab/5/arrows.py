base = int(input())
half = int((base / 2) + 1)

# HALF, STARS
for stars in range(1,half+1,1):
    row = '*' * stars
    print(row)
for stars in range(half-1,0,-1):
    row = '*' * stars
    print(row)


# HALF, STARS, CIRCLE ENDS
for stars in range(1,half+1,1):
    row = '*' * (stars-1)
    row += 'o'
    print(row)
for stars in range(half-1,0,-1):
    row = '*' * (stars-1)
    row += 'o'
    print(row)


# FULL, CENTER CIRCLE, INNER STARS, OUTER CIRCLES
"""
--*--
-o*o-

"""

stars = 0
circles = 0

for row in range(base):
    stars = 
    


# FULL, OUTER STARS
