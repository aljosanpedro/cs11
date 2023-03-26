VOWELS = "aeiou"
vowel_count, consonant_count = 0,0

print()
while True:
    word = input("Word [letters only]: ")
    valid_word = True
    
    for character in word:
        if not character.isalpha():
            valid_word = False
            break
    
    if not valid_word:
        print("Input should be a word.\n")
        continue
    
    print()
    break


for letter in word:
    if letter in VOWELS:
        vowel_count += 1
    else:
        consonant_count += 1
        
        
print("No. of vowels:", vowel_count)
print("No. of consonants:", consonant_count)
print()