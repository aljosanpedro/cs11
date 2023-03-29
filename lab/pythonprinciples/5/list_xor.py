def main():
    print(list_xor(1, [1, 2, 3], [4, 5, 6]))
    

def list_xor(n, list1, list2):
    is_n_exclusive = False
    
    if (n in list1) ^ (n in list2):
        is_n_exclusive = True
        
    return is_n_exclusive     


main()

"""
def list_xor(n, list1, list2):
    is_n_exclusive = False
    
    if ((n in list1) and (not n in list2) or
        (n in list2) and (not n in list1)):
            is_n_exclusive = True
    
    return is_n_exclusive
"""
