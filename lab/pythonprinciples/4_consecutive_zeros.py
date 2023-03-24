def main():
    print(consecutive_zeros("1001101000110"))


def consecutive_zeros(binary_string):
    consecutive_zeros, most_consecutive_zeros = 0,0
    
    for character in binary_string:
        
        character = int(character)
        if character == 0:
            consecutive_zeros += 1
        else:
            consecutive_zeros = 0
            
        if consecutive_zeros > most_consecutive_zeros:
            most_consecutive_zeros = consecutive_zeros
    
    return most_consecutive_zeros
    
    
main()