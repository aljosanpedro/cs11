SPLIT_SEPARATOR = ','

PRIME, COMPOSITE, NEITHER = "Prime", "Composite", "Neither"
FACTORS_LIMIT = 10


def main():
    numbers = input() # "2,5,9,3,1,10"
    numbers = format_input(numbers)
    
    for number in numbers:
        is_prime = test_prime(number)
        factors = calculate_factors(number)
        
        print(f"{number} is {is_prime} with factors {factors}")
    
    
def format_input(numbers_str):
    numbers_int = []
    
    numbers_str = numbers_str.split(SPLIT_SEPARATOR) # ['2','5','9','3','1','10']

    for number in numbers_str:
        number = int(number)
        numbers_int.append(number)

    return numbers_int # [2, 5, 9, 3, 1, 10]


def test_prime(number):    
    # neither prime nor composite if 1 or negative
    if number <= 1:  
        return NEITHER
    
    # test if composite
        # concern: inefficient with very large numbers
    for i in range(1,number+1):
        # ignore prime conditions
        if (i == 1) or (i == number):
            continue
        
        # divisible by a number not 1 or itself
        if number % i == 0:
            return COMPOSITE
    
    # prime if reaches this line
    return PRIME
    
    
def calculate_factors(number):
    factors = []
    
    for i in range(1,FACTORS_LIMIT): # range strictly positive
        # factor if no remainder
        if number % i == 0:
            factors.append(i)
    
    return factors


main()
