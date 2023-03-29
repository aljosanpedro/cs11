def main():
    print(palindrome("abc"))
    
    
def palindrome(normal_word):
    is_palindrome = False
    
    reverse_word = normal_word[::-1]
    
    if normal_word == reverse_word:
        is_palindrome = True
    
    return is_palindrome
    

main()
