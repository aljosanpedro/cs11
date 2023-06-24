SEPARATOR = ' '
COMPRESSION_FACTOR = 5

Y_RANGE = range(-5,6,1)
X_RANGE = range(-5,6,1)

POINT_TEXT = ' * '
BLANK_TEXT = '   '



def main():
    # INPUT
    print("---INPUT--- \n")
    coefficients = input_numbers_list("coefficients")
    exponents = input_numbers_list("exponents")
    print()
    

    # OUTPUT
    print("---OUTPUT--- \n")
    points = generate_points(coefficients, exponents)
    final_points = grapher(points)
    inverted_points = function_inverse(final_points)
    function_or_relation(inverted_points)


def input_numbers_list(numbers_type):
    while True:
        numbers = input(f"{numbers_type.title()} [ex. 1{SEPARATOR}2{SEPARATOR}3]: ").strip()
        numbers = numbers.split(sep=SEPARATOR)
        
        for index in range(len(numbers)):
            number = numbers[index]
            
            if not number.isdecimal():
                print("Input Error: Input should be numbers divided by spaces only.")
                continue
            
            numbers[index] = int(number)
            
        print(f"{numbers_type.title()}: {numbers} \n")
        
        return numbers


def sort_points(points):
    # confirmed: list.sort() works for tuples in a list
    
    points.sort()

    return points


def generate_points(coefficients, exponents):
    points = [] # [(x1,y1), (x2,y2), ...]

    
    # List length checking
    if not len(coefficients) == len(exponents):
        print("Error: Unequal Lengths of Coefficients and Exponents Lists")
        return


    # Print equation
    equation = "y = "
    
    for index in range(len(exponents)):
        coefficient, exponent = coefficients[index], exponents[index]
        
        term = str(coefficient) + 'x' + '^' + str(exponent)
        
        if not index == len(exponents) - 1:
            term += ' + '
        
        equation += term
        
    print(f"Polynomial Equation: {equation} \n")
    
    
    # Generate points
    for x in X_RANGE:
        y = 0
        
        for index in range(len(exponents)):
            coefficient, exponent = coefficients[index], exponents[index]
            
            product = coefficient * pow(x, exponent)
            
            y += product
            
        points.append((x,y))
    
    # no need to sort points (tuples) bc loop from -5,5 already


    print(f"Generated Points: \n {points} \n")
    return points


def grapher(points):
    # Prepare points
    compressed_points = compress_points(points, COMPRESSION_FACTOR)
    final_points = [] # replace pts w/ compressed pts if outside X or Y ranges
    
    for index in range(len(points)):
        (x,y) = points[index] # (x,y)
        
        # Use compressed y if beyond range
        if not y in Y_RANGE:
            compressed_point = compressed_points[index]
            y = compressed_point[1] # (x,y), y = index 1
        
        final_points.append((x,y))
        
    print(f"Final Points: \n {final_points} \n")
    
    
    # Print graph
    print("Compressed Graph:")
        
    for row in range(len(Y_RANGE)): # 0 -> 11, not -5 -> +5, bc easier to access elements
        row_text = ''
        
        column_correction = int(len(X_RANGE) / 2)
        row_correction = int(len(Y_RANGE) / 2)
        
        for column in range(len(X_RANGE)):
            # row index: 0 -> x = 5; subtract half of length of row range
            # column index: 0 -> y = -5 ; subtract same, but opposite sign
            
            
            point = (column-column_correction, ((row-row_correction) * -1))
            
            if point in final_points:
                row_text += POINT_TEXT
            else:
                row_text += BLANK_TEXT            
            
        print(row_text)
        
    print()
      
        
    return final_points # to remove; for testing guide examples only
            

def compress_points(points, n):
    compressed_points = []
    
    
    # Check compression factor 'n'
    if n < 0:
        print("Error: Compression Factor not Positive Integer")
        return
    
    # Compress points
    for point in points:
        (x,y) = point
        
        modulo = abs(y) % COMPRESSION_FACTOR # acted weird when y was negative -> absolute value
        
        # If negative before compression, retain negative
        if y < 0:
            modulo *= -1
        
        y = modulo
        
        point = (x,y)
        compressed_points.append(point)
    
    # no need to call sort_points(points) bc loop from -5,5 already
    
    print(f"Compressed Points: \n {compressed_points} \n")
    return compressed_points


def function_inverse(points):
    inverse_points = []
    
    
    for point in points:
        (x,y) = point
        inverse_points.append((y,x))
        
        
    print(f"Inverse Points: \n {inverse_points} \n")        
    return sort_points(inverse_points)
    

def print_mapping_of_values(points):
    value_map = {}
    
    
    points = sort_points(points)

    for point in points:
        (x,y) = point
        
        if not x in value_map.keys():
            value_map[x] = [y]
        else:
            value_map[x].append(y)
    
    
    print("Value Map:")
    
    for x in value_map:
        print(f"{x} : {value_map[x]}")
        
    print()
    

def function_or_relation(points):
    is_function = True
    
    
    points = sort_points(points)
    value_map = {}
        
        
    for point in points:
        (x,y) = point
        
        if not x in value_map.keys():
            value_map[x] = [y]
        else:
            value_map[x].append(y)
    
    
    for x in value_map:
        if not len(value_map[x]) == 1: # function if x maps to only 1 y
            is_function = False
    
    
    print("Relationship:")
    
    if is_function:
        print("Function \n")
    else:
        print("Relation \n")
        
        # if relation, print value map
        print("Value Map:")
        
        for x in value_map:
            print(f"{x} : {value_map[x]}")
        
        print()
    
    return is_function



main()
