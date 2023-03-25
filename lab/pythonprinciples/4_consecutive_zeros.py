def main():
    print(consecutive_zeros("1001101000110"))


def consecutive_zeros(binary_string):
    consecutive_zeros, most_consecutive_zeros = 0,0
    
    for number in binary_string:
        if number == '1':
            consecutive_zeros = 0
            continue
        
        consecutive_zeros += 1
            
        if consecutive_zeros > most_consecutive_zeros:
            most_consecutive_zeros = consecutive_zeros
    
    return most_consecutive_zeros
    
    
main()