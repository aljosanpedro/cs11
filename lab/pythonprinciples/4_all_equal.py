def main():
    print(all_equal([1,1,1]))


def all_equal(list):
    has_same = True
    list_length = len(list)
    
    for index in range(list_length):
        if index < list_length - 1:
            
            current_element, next_element = list[index], list[index + 1]
            if not current_element == next_element:
                has_same = False

    return has_same


main()
