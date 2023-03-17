n = int(input("Element number (int): "))
a,b = 0,1


for i in range(n - 1):
    c = a + b
    a,b = b,c


print("nth element in Fibonacci Sequence:", c)
