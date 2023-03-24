def main():
    print(is_anagram("typhoon", "opython"))
    
    
def is_anagram(word1, word2):
    is_anagram = False
    
    word1, word2 = list(word1), list(word2)
    
    word1.sort()
    word2.sort()
    
    if word1 == word2:
        is_anagram = True
    
    return is_anagram
    
    
main()
