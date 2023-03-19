# INPUT
print("The program will ask for a positive odd number of rows.")
print("It will then print a pyramid with that many rows.\n")

while True:
    BASE = float(input("How many rows [positive odd integer]?: "))
    
    if (BASE <= 0 or 
        BASE % 2 == 0 or 
        not BASE.is_integer()):
        
        print("Invalid input.\n")
    else:
        break
    

# PROCESS, OUTPUT (prints)
print(f"\nOutput when BASE = {int(BASE)}:")


HALF = int((BASE / 2) + 1)

for i in range(1,HALF,1):
    row = '*'
    row *= i
    
    print(row)
    
for i in range(HALF,0,-1):
    row = '*'
    row *= i
    
    print(row)
