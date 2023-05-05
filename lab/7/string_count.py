def main():
    string = input("String: ")
    letter = input("Letter to count in string: ")
    
    letter_count = count(string, letter)
    
    print()
    print(f"The letter \'{letter}\' is in \"{string}\" {letter_count} times")
    print()


def count(string, letter):
    count = 0
    
    for character in string:
        if character == letter:
            count += 1
    
    return count


main()
