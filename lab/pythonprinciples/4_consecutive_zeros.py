def main():
    print(consecutive_zeros("1001101000110"))


def consecutive_zeros(binary):
    # ex ."1001101000110"
    consec, largest = 0,0
    
    for char in binary:
        if int(char) == 0:
            consec += 1
        else:
            consec = 0
            
        if consec > largest:
            largest = consec
    
    return largest
    
    
main()