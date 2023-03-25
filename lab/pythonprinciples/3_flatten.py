def main():
    print(flatten([[1,2],[3,4]]))


def flatten(list_2d):
    flat_list = []
    
    list_2d_length = len(list_2d)
    
    for sublist_index in range(list_2d_length):
        sublist = list_2d[sublist_index]
        sublist_length = len(sublist)
        
        for element_index in range(sublist_length):
            element = list_2d[sublist_index][element_index]
            
            flat_list.append(element)
    
    return flat_list


main()
