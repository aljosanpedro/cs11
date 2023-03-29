x = int(input())
y = int(input())

base = x

if y == 0:
    print(1)
else:
    for _ in range(y-1): # -1 because x^1 as base
        x *= base
        
    print(x)
