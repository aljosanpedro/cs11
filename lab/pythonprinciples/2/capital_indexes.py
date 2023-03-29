def main():
    print(capital_indexes("HeLlO"))


def capital_indexes(string):
    indexes = []
    
    for index in range(len(string)):
        letter = string[index]
        
        if letter.isupper():
            indexes.append(index)
    
    return indexes
    
    
main()