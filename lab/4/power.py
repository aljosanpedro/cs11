x = int(input())
y = int(input())

base = x
count = 1

if y == 0:
    print(1)
else:
    while count < y:
        x = x * base
        count += 1
    print(x)
