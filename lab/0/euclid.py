m = int(input("1st number: "))
n = int(input("2nd number: "))

if m > n:
    big, small = m, n
else:
    big, small = n, m
    
    
while True:
    remainder = big % small
    
    if remainder == 0:
        gcf = small      
        break
    else:
        big, small = small, remainder
        
        
print(f"GCF of {m} and {n} is {gcf}")
