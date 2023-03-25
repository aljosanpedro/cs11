def main():
    print(all_equal([1,1,1]))


def all_equal(list):
    is_all_equal = True
    
    list_range = range(len(list))
    list_max_index = list_length - 1
    
    for index in list_range:
        
        if index < list_max_index:
            current_element = list[index]
            next_element = list[index + 1]
            
            if not current_element == next_element:
                is_all_equal = False

    return is_all_equal


main()
