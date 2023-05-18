def main():
    while True:
        number = int(input("Positive int: "))
        
        if number > 0:
            break
        
        
    is_prime = prime(number)
    
    print(is_prime)
    

def prime(number):
    for i in range(1, number + 1):
        if i == 1 or i == number: 
            continue
        
        if number % i == 0:
            return False

    return True


main()
