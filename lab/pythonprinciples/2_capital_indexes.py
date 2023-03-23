def main():
    print(capital_indexes("HeLlO"))


def capital_indexes(string):
    indeces = []
    
    for index in range(len(string)):
        if string[index].isupper():
            indeces.append(index)
    
    return indeces
    
    
main()