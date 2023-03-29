def main():
    print(double_letters("hello"))


def double_letters(word):
    is_double = False
    
    word_length = len(word)
    break_index = word_length - 1
    
    for index in range(word_length):
        
        if index == break_index:
            break
        
        current_word = word[index]
        next_word = word[index + 1]
        
        if not current_word == next_word: 
            is_double = True
                
    return is_double


main()
