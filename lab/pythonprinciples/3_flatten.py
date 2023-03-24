def main():
    print(flatten([[1,2],[3,4]]))


def flatten(list_2d):
    flat_list = []

    list_2d_length = len(list_2d)
    for sublist in range(list_2d_length):
        for element in range(list_2d_length[sublist]):
            
            flat_list.append(list_2d[sublist][element])
    
    return flat_list


main()
