def main():
    binary = input("Binary String [ex. 10010110]: ")
    
    decimal = binary_converter(binary)
    
    print(f"Decimal Value: {decimal}")


def binary_converter(binary):
    decimal = 0
    
    for i in range(len(binary)):
        number = binary[i]
        number = int(number)
        
        exponent = len(binary) - i - 1
        
        value = pow(2, exponent)
        
        if number == 1:
            decimal += value
        
    return decimal


main()
