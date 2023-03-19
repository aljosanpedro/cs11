n = int(input())

a,b = 0,1


print(b)

for i in range(n-1):
    c = a + b

    a,b = b,c

    
    print(c)
