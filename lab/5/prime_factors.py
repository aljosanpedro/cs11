# INPUT
number = int(input())

factors, prime_factors = [], []


# FACTORS
for possible_factor in range(number + 1 , 0, -1):
    if number % possible_factor == 0:
        factors.append(possible_factor)
        
factors.sort()

        
# PRIME FACTORS
for factor in factors:
    is_prime = True
    
    if factor == 1:
        continue
    
    for possible_prime in range(1, number + 1):
        
        if (possible_prime == 1) or (possible_prime == factor):
            continue
        
        if factor % possible_prime == 0:
            is_prime = False
            break
        
    if not is_prime:
        break

    prime_factors.append(factor)
 
      
# OUTPUT 
print(f"Factors of {number}: {factors}")
print(f"Prime factors of {number}: {prime_factors}")
