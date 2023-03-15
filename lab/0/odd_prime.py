def main():
    n = check_input()
    flag = check_odd_prime(n)
    
    print("Is input NOT an odd prime number?:", flag)
    

def check_input():
    while True:
        n = int(input("Odd number greater than 2: "))
        
        if (not n % 2 == 0) and (n > 2):
            break
        
    return n
    

def check_odd_prime(n):
    flag = False
    
    i = 2  
    while True:
        if n % i == 0:
            flag = True
                
        i += 1
        j = (n / 2) + 1
        
        if not i < j:
            break
        
    return flag


main()
