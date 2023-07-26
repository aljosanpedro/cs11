"""
Alejandre Jose "Aljo" San Pedro
CS 11 LAB 1
"""


def generate_points(coefficients, exponents):
    # constants, set to preference
    X_SIZE = 5 # half-length of graph
    
    # list length checking
    if not len(coefficients) == len(exponents):
        return    
    
    # generate points
    points = []
    
    for x in range(-X_SIZE, X_SIZE + 1): # from lowest to highest x
        y = 0 # reset y to 0 every term
        
        for index in range(len(exponents)):
            # used index vs. elements
                # bc coefficients and exponents indeces are the same
            coefficient, exponent = coefficients[index], exponents[index]
            
            y += coefficient * pow(x, exponent) # add up value of each term
                        
        points.append((x,y)) # fill up list of coords
    
    # sorting
        # no need to sort points (tuples)
            # bc loop from lowest/negative to highest/positive already
            # but, if ever need to sort, can uncomment next line
            
    # points.sort()
        
    # output
    return points


def grapher(points):
    # constants (set to preference)
    COMPRESSION_FACTOR = 5 # 'n'
    
    X_SIZE = 5 # half of length of graph
    Y_SIZE = 5 # half of height of graph
    
    POINT_CHAR = '*' # point in graph
    BLANK_CHAR = '_' # empty space in graph
    
    # prepare points
    final_points = []
    
        # gather compressed version of all points
    compressed_points = compress_points(points, COMPRESSION_FACTOR)
    
    for index in range(len(points)):
        # used index vs. elements bc used same index on different lists

        (x,y) = points[index] # (x,y)        
        (compressed_x, compressed_y) = compressed_points[index] # compressed (x,y)
        
        # replace x and/or y with compressed versions if outside x/y ranges
        if not -X_SIZE < x < X_SIZE:
            x = compressed_x
        if not -Y_SIZE < y < Y_SIZE: # not elif bc can be both x & y out of ranges
            y = compressed_y
        
        final_points.append((x,y)) # replace points that need compressed versions
               
    # generate graph    
    graph = ''
    
    for row in range(2 * Y_SIZE): # 2x to accommodate negative <-> positive
        # used len(range), not range itself
            # ex. 0 -> 11, not -5 -> +5
            # bc easier to access elements with row/column as indeces from 0
        
        row_text = '' # fills with points/blanks on a row
        
        for column in range(2 * X_SIZE):
            # subtract correction factors from row/column index later
                # converts indeces to actual values
                # row index: 0 -> x = 5
                    # subtract half of length of row range
                # column index: 0 -> y = -5
                    # subtract same, but opposite sign
            point = (column-X_SIZE, ((row-Y_SIZE) * -1))
            
            # determine if a coord has a point -> assign char -> add to row text            
            if point in final_points:
                row_text += POINT_CHAR
            else:
                row_text += BLANK_CHAR
            
        graph += f"{row_text} \n"
    
    # output
    print(graph) # only print allowed
    
    return graph
            

def compress_points(points, n):
    # check compression factor 'n'
        # should be positive
    if n < 0:
        return
    
    # compress points
    compressed_points = []
    
    for point in points:
        (x,y) = point
        
        # acted weird when negative -> use absolute value
        modulo_x = abs(x) % n
        modulo_y = abs(y) % n 
        
        # if negative before compression, retain negative sign
        if x < 0:
            modulo_x *= -1
        if y < 0: # not elif because can be both negative
            modulo_y *= -1
        
        x,y = modulo_x,modulo_y # compressed values
                
        compressed_points.append((x,y))
        
    # output
    compressed_points.sort() # confirmed: list.sort() works for tuples in a list
        
    return compressed_points


def function_inverse(points):
    # inverse
    inverse_points = []
    
    for point in points:
        (x,y) = point
        inverse_points.append((y,x)) # flip x & y
    
    # output
    inverse_points.sort()
                
    return inverse_points
    

def print_mapping_of_values(points):
    # assign values
    points.sort()
    
    value_map = {}
    
    for point in points:
        (x,y) = point
        
        if not x in value_map.keys():
            # make a new key (x)-value (y) pair if none for x
            value_map[x] = [y]
        # specific condition instead of else to avoid duplicate values
        elif y not in value_map[x]:
            # assign other values of y to existing x keys
            value_map[x].append(y)
    
    # output
    value_map_text = ''
    
    for x in value_map:
        
        y_values = value_map[x]
        y_text = '' # hold y values mapped to x without list brackets []
                
        for index in range(len(y_values)):
            y = y_values[index]
        
            y_text += str(y)
            
            # used indeces to break before last element
                # to avoid comma at end
            if index == len(y_values) - 1:
               break
           
            y_text += ', '
            
        value_map_text += f"{x} : {y_text} \n"
        
    return value_map_text
        

def function_or_relation(points):
    # assign values
        # replicate value_map from print_mapping_of_values
            # but without the formatted output string (i.e. x : [y1, y2, ...] \n)
            # could be a function instead shared with print_mapping_of_values
                # composition design
    points.sort()
    
    value_map = {}
    
    for point in points:
        (x,y) = point
        
        if not x in value_map.keys():
            value_map[x] = [y]
        elif y not in value_map[x]:
            value_map[x].append(y)
    
    # determine relationship
    is_function = True
    
    for x in value_map:
        # is a function if x maps to only 1 y
        if len(value_map[x]) > 1:
            is_function = False
     
    # output
    if is_function:
        # if function, return True
        return True
    else:
        # if relation, return formatted value map        
            # could also be a shared function with print_mapping_of_values (composition)
        value_map_text = ''
    
        for x in value_map:
            
            y_values = value_map[x]
            y_text = '' # hold y values mapped to x without list brackets []
                    
            for index in range(len(y_values)):
                y = y_values[index]
            
                y_text += str(y)
                
                # used indeces to break before last element
                    # to avoid comma at end
                if index == len(y_values) - 1:
                    break
            
                y_text += ', '
                
            value_map_text += f"{x} : {y_text} \n"
            
        return value_map_text
            
