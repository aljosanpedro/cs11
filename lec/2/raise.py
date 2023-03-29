x = int(input())
y = int(input())

result = x


if y == 0:
    result = 1
else:    
    for _ in range(1,y):
        result *= x

    
print(result)
