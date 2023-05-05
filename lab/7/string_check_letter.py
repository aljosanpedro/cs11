def main():
    string = input("String: ")
    letter = input("Letter to check if in string: ")
    
    is_letter_in_string = checkLetter(string, letter)
    
    if is_letter_in_string:
        message = "IS"
    else:
        message = "IS NOT"
        
    print()
    print(f"The letter \'{letter}\' {message} in \"{string}\"")
    print()


def checkLetter(string, letter):
    is_letter_in_string = False
    
    for character in string:
        if character == letter:
            is_letter_in_string = True
            break
    
    # Alternative Method
    """
    if letter in string:
        is_letter_in_string = True
    """
    
    return is_letter_in_string


main()
