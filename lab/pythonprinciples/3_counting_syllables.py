def main():
    print(count("ter-min-a-tor"))


def count(word):
    syllables = word.split('-')
    
    return len(syllables)
    
    
main()
