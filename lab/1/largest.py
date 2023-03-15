NUMBERS = 3
largest = 0


for _ in range(NUMBERS):
    current = int(input())
    
    if current > largest:
        largest = current
    
    
print(largest)
    