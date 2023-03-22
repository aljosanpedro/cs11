def main():
    VOWELS = "aeiou"
    # using lists only; no dictionaries
    vowels_counts, consonants_counts = [[],[]], [[],[]]

    word = input_word()

    for letter in word:
        if letter in VOWELS:
            update_count(letter, vowels_counts)
        else:
            update_count(letter, consonants_counts)

    print_counts("Vowel", vowels_counts)
    print_counts("Consonant", consonants_counts)


def input_word():
    print()
    while True:
        word = input("Input a word [letters only]: ")
        
        valid = True
        
        for character in word:
            if not character.isalpha():
                valid = False
                break
        
        if not valid:
            print("Invalid input.\n")
            continue
        
        print()
        break

    return word


def update_count(letter, counts):
    if not letter in counts[0]:
        counts[0].append(letter)
        counts[1].append(1)
    else:
        index = counts[0].index(letter)
        counts[1][index] += 1
        

def print_counts(count_type, counts):
    print(f"{count_type} Counts:")
    
    for index in range(len(counts[0])):
        print(f"{counts[0][index]}: {counts[1][index]}")
        
    print()
    
        
main()
