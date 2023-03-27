def main():
    print(format_number(100000))
    
    
def format_number(number):
    formatted_number = ""
    
    number = str(number)[::-1]

    for index in range(len(number)):
        digit = number[index]
        index += 1 # 0 index -> 1
        
        formatted_number += digit
        
        if (not index == len(number)) and (index % 3 == 0):
            formatted_number += ','
    
    formatted_number = formatted_number[::-1]
    
    return formatted_number
    
    
main()
