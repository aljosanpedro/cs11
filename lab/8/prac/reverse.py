def main():
    letters = input("Letters: ")
    
    letters_reverse = reverse(letters)
    
    print(letters_reverse)


def reverse(letters):
    letters_reverse = ""
    
    # regular solution
    for i in range(len(letters)-1, -1, -1):
        letter = letters[i]
        letters_reverse += letter
    
    # shortcut solution
    # letters_reverse = letters[::-1]

    return letters_reverse


main()
