# INPUT
print("The program will ask for a positive odd number of rows.")
print("It will then print a pyramid with that many rows.\n")

BASE = get_base()


# PROCESS, OUTPUT (prints)
print(f"\nOutput when BASE = {int(BASE)}:")

HALF = int((BASE / 2) + 1)

for top_index in range(1,HALF,1):
    print_row(top_index)
    
for bottom_index in range(HALF,0,-1):
    print_row(bottom_index)
    

# FUNCTIONS
def get_base():
    BASE = 0
    
    while True:
        BASE = float(input("How many rows [positive odd integer]?: "))
        
        if (BASE <= 0 or 
            BASE % 2 == 0 or 
            not BASE.is_integer()):
            
            print("Invalid input.\n")
            continue
        
        break
    
    return BASE
    

def print_row(row_length):
    row = '*'
    row *= row_length
    
    print(row)
