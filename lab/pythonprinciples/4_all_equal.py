def main():
    print(all_equal([1,1,1]))


def all_equal(list):
    same = True
    
    for index in range(len(list)):
        if index < len(list)-1:
            if list[index] != list[index+1]:
            same = False

    return same


main()
