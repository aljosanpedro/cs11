VOWELS = "aeiou"
vowel_count, consonant_count = 0,0

while True:
    word = input("Word [letters only]: ")
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


for letter in word:
    if letter in VOWELS:
        vowel_count += 1
    else:
        consonant_count += 1
        
        
print("No. of vowels:", vowel_count)
print("No. of consonants:", consonant_count)
print()