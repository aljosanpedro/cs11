def main():
    print(mid("abc"))


def mid(string):
    character = ''
    
    string_length = len(string)
    if string_length % 2 != 0:
        index = int(string_length / 2)
        
        character = string[index]
    
    return character
    
    
main()