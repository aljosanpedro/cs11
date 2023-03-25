def main():
    print(flatten([[1,2],[3,4]]))


def flatten(list_2d):
    flat_list = []
    
    for sublist_index in range(len(list_2d)):
        sublist = list_2d[sublist_index]
        
        for element_index in range(len(sublist)):
            element = sublist[element_index]
            
            flat_list.append(element)
    
    return flat_list


main()
