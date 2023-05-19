def main():
    phrase_A = input("First Phrase: ").lower()
    phrase_B = input("Second Phrase: ").lower()
    
    are_anagrams = checkAnagram(phrase_A, phrase_B)
    
    if are_anagrams:
        print("YES, the phrases are anagrams")
    else:
        print("NOT ANAGRAMS")


def checkAnagram(phrase_A, phrase_B):
    # enough loops by using longer phrase
    if len(phrase_A) < len(phrase_B): 
        phrase_B, phrase_A = phrase_A, phrase_B
    
    # placeholder phrases since need to remember original phrase
    temp_A, temp_B = phrase_A, phrase_B
    
    # remove all spaces
    temp_A = temp_A.replace(' ', '')
    temp_B = temp_B.replace(' ', '')
    
    # convert to list so can use list.remove()
    temp_A, temp_B = list(temp_A), list(temp_B)
    
    for char in phrase_A:
        # ignore space since can't remove in str phrase_A?
        if char == ' ':
            continue
        
        # delete chars from lists until only unique ones left
        if (char in temp_A) and (char in temp_B):
            temp_A.remove(char)
            temp_B.remove(char)
    
    # anagram if no unique chars
    if (temp_A == []) and (temp_B == []):
        return True
    else:
        return False
    

main()
