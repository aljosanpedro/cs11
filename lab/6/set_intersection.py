def main():
    # input
    X = input()
    Y = input()
    
    # input formatting
    X_ints, Y_ints = [], []
    
    X_ints = convert_list(X, X_ints)
    Y_ints = convert_list(Y, Y_ints)
    
    # intersection
    Z = []
    
        # use shorter list as base to check longer list -> ensures enough checks
    shorter, longer = X_ints, Y_ints
    if (len(X_ints) > len(Y_ints)) or (len(X_ints) == len(Y_ints)):
        shorter, longer = Y_ints, X_ints
        
    for number in shorter:
        # 2nd condition to make unique
        if (number in longer) and (not number in Z):
            Z.append(number)
            
    Z.sort()

    # output
    if len(Z) == 0:
        print("intersection is empty")
    else:
        print(Z)
    

def convert_list(str_list, int_list):
    str_list = str_list.split(' ')
    
    for number in str_list:
        # catch an error that kept happening
        if number == '':
            continue
        
        number = int(number)
        int_list.append(number)    
    
    return int_list


main()
