def main():
    print(only_ints('a',2))
    
    
def only_ints(a,b):
    are_only_ints = False
    
    if (type(a) is int) and (type(b) is int):
        are_only_ints = True
    
    return are_only_ints


main()