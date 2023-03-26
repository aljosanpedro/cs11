def main():
    print(div_3(6))
    

def div_3(number):
    is_divisible = False
    
    if number % 3 == 0:
        is_divisible = True
    
    return is_divisible
    
    
main()
