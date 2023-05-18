LIST_SEPARATOR = " "

def main():
    numbers = input_numbers()
    
    even_count, odd_count = even_odd(numbers)
    
    print(f"Number of Even Numbers: {even_count}")
    print(f"Number of Odd Numbers: {odd_count}")
    
    
def input_numbers():
    while True:
        numbers_temp = input(f"List of integers [format: 1{LIST_SEPARATOR}2{LIST_SEPARATOR}3]: ") # "1, 2, 3"
        numbers_temp = numbers_temp.split(sep = LIST_SEPARATOR) # ['1', '2', '3']        
        
        numbers = [] # [1, 2, 3]
        
        is_numbers_valid = True
        
        for number in numbers_temp:
            if not number.isdigit(): # str.is_digit checks floats bc ONLY digits
                print("All numbers should be integers.")
                
                is_numbers_valid = False
                break
            
            number = int(number)
            numbers.append(number)
        
        if is_numbers_valid:
            break
        
    return numbers
    

def even_odd(numbers):
    even_count, odd_count = 0, 0
    
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return (even_count, odd_count)


main()
