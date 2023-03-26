def main():
    print(is_anagram("typhoon", "opython"))
    
    
def is_anagram(word1, word2):
    is_anagram = False
    
    word1 = sort_word(word1)
    word2 = sort_word(word2)
    
    if word1 == word2:
        is_anagram = True
    
    return is_anagram


def sort_word(word):
    
    word = list(word)
    word.sort()
    
    return word
    
    
main()
