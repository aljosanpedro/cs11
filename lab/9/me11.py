PUNCTUATION_MARKS = ".,:;?()[]\"\'!_/\\@}{*#$%^&+=|<>~`”“"
NO_SPACE = ''
SEPARATOR = ' '



def main():
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
    
    
    words_to_counts = {}
    
    for word in words:
        if word in words_to_counts.keys():
            words_to_counts[word] += 1
        else:
            words_to_counts.update({word : 1})
                
    # formatted printing
    for word in words_to_counts.keys():
        count = words_to_counts[word]
        
        print(f"{word} : {count}")

main()
