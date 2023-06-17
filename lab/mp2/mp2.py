COMPRESSION_FACTOR = 5


def main():
    
    #points = [(5,6), (3,4), (1,2)]
    
    coefficients = [1,2,4]
    exponents = [2,3,1]
    
    print(f"Coefficients: {coefficients}")
    print(f"Exponents: {exponents}")
    print()
    
    # coefficients = [1]
    # exponents = [2]

    points = generate_points(coefficients, exponents)
    final_points = grapher(points)
    inverted_points = function_inverse(final_points)
    function_or_relation(inverted_points)



def sort_points(points):
    # confirmed: list.sort() works for tuples in a list
    # to-do: manual via sorting algo?
    
    points.sort()

    return points



def generate_points(coefficients, exponents):
    # Initializations
    points = [] # [(x1,y1), (x2,y2), ...]
    c,e = coefficients, exponents # for convenience

    
    # List length checking
    if not len(c) == len(e):
        print("Error: Unequal Lengths of Coefficients and Exponents Lists")
        return


    # Print equation
    equation = "y = "
    
    for i in range(len(e)):
        term = str(c[i]) + 'x' + '^' + str(e[i])
        
        if not i == len(e) -1:
            term += ' + '
        
        equation += term
        
    print(f"Polynomial Equation: {equation} \n")
    
    
    # Generate points
    for x in range(-5,6,1):
        y = 0
        
        for i in range(len(e)):                        
            product = c[i] * pow(x,e[i])
            
            y += product
            
        points.append((x,y))
    
    # no need to call sort_points(points) bc loop from -5,5 already


    print(f"Generated Points: \n {points} \n")    
    return points


def grapher(points):
    # Prepare points
    compressed_points = compress_points(points, COMPRESSION_FACTOR)
    final_points = []
    
    for i in range(len(points)):
        (x,y) = points[i] # (x,y)
        
        # Use compressed y if beyond range
        if not -5 <= y <= 5:
            compressed_point = compressed_points[i]
            y = compressed_point[1]
        
        final_points.append((x,y))
        
    print(f"Final Points: \n {final_points} \n")
    
    
    # Print graph
    print("Compressed Graph:")
        
    for row in range(11):
        row_text = ''
        
        for column in range(11):
            # row index: 0 -> x: -5; subtract 5
            # column index: 0 -> y: 
            point = (column-5, ((row-5) * -1))
            
            if not point in final_points:
                is_point = '   '
            else:
                is_point = ' * '
                
            row_text += is_point
            
            
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
        
        modulo = abs(y) % 5 # acted weird when y was negative -> absolute value
        
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
        if not len(value_map[x]) == 1:
            is_function = False
    
    
    if is_function:
        print("Points are a Function. \n")
    else:
        print("Points are a Relation. \n")
        
        print("Value Map:")
        for x in value_map:
            print(f"{x} : {value_map[x]}")
        print()
    
    return is_function



main()
