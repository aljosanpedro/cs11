def main():
    print(all_equal([1,1,1]))


def all_equal(List):
    is_all_equal = True
    
    list_length = len(List)
    list_break_index = list_length - 1
    
    for index in range(list_length):
        
        if index == list_break_index:
            break
            
        current_element = List[index]
        next_element = List[index + 1]
            
        if not current_element == next_element:
            is_all_equal = False

    return is_all_equal


main()
