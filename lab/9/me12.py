PUNCTUATION_MARKS = ".,:;?()[]\"\'!_/\\@}{*#$%^&+=|<>~`”“"
NO_SPACE = ''
SEPARATOR = ' '



def main():
    # TEXT
    text = input()
    
    # handles same words but upper/lowercase
    text = text.lower()
        
    # removes all punctuation marks except dashes
    for mark in PUNCTUATION_MARKS:
        text = text.replace(mark, NO_SPACE)
            
    words = text.split(SEPARATOR)    
        
    # remove dashes that are not between words
    for i in range(len(words)):
        word = words[i]
        words[i] = word.strip('-')
        
    # "sorts" the list beforehand so dictionary sorts itself while counting
    words = sorted(words)
    
    
    # SEARCH WORDS
    search_words = input() # "processing is the next step"
    search_words = search_words.split(' ') # ["processing", "is", "the", "next", "step"]
    
        
    # WORDS COUNTS
    # make dictionary using search word list
    search_words_to_counts = {}
    
    for word in search_words:
        search_words_to_counts.update({word : 0})
        
    # count words found in search list
    for word in words:
        if word in search_words_to_counts.keys():
            search_words_to_counts[word] += 1
            
                
    # formatted printing
    for word in search_words_to_counts.keys():
        count = search_words_to_counts[word]
        
        print(f"{word} : {count}")

main()
