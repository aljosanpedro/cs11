def main():
    print(double_letters("hello"))


def double_letters(word):
    is_double = False
    word_length = len(word)
    
    for index in range(word_length):
        
        if index == word_length - 1:
            break
        
        if not word[index] == word[index+1]: 
            is_double = True
                
    return is_double


main()
