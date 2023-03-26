def main():
    print(count("ter-min-a-tor"))


def count(word):
    syllables = word.split('-')
    syllables_count = len(syllables)
    
    return syllables_count
    
    
main()
