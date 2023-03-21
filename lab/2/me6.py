"""
i = 0,1,2,3,4,5
f = 1,1,2,3,5,8
    a b c
      a b c
        a b c
a = fib[0] -> fib[i]
b = fib[1] -> fib[i+1]
c = fib[2] -> fib[i+2]
"""

n = int(input())

fib = [1,1]


for i in range(n):
    fib.append(fib[i] + fib[i+1])
    
    
    print(fib[i])
    
"""
# old version
n = int(input())
a,b = 1,1

for i in range(n-1):
    c = a + b
    a,b = b,c

    print(a)
"""
