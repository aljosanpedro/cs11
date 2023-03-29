while True:
    a = int(input("Smaller number: "))
    b = int(input("Bigger number: "))

    if not a < b:
        print("Input smaller number first.")
    else:
        break
    
    
while True:
    if a % 2 == 0:
        print(f'{a }')
        
    a += 1
    
    if not a <= b:
        break
    