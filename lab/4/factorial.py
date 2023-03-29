number = int(input())
factorial = 1

for i in range(number,1,-1):
    factorial *= i
    
print(factorial)
