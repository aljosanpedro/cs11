while True:
    m = int(input("1st number [bigger]: "))
    n = int(input("2nd number [smaller]: "))

    if m <= n:
        print("\nInvalid input.\n")
    else:
        break
    
    
while True:
    r = m % n
    
    if r != 0:
        m,n = n,r
    else:
        gcf = n      
        break
        
        
print(f"\nGCF is {gcf}.\n")
