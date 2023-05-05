"""
ALEJANDRE JOSE R. SAN PEDRO
LAB 1
"""


VOWELS = "aeiouAEIOU"

letters = input("String of letters: ")


vowel_count = 0
consonants_count = 0

vowels_once = []

for letter1 in letters:
    if letter1 in VOWELS:
        vowel_count += 1
    else:
        consonants_count += 1


    vowel_once_count = 0

    for letter2 in letters:
        if ((letter1 in VOWELS) and 
            (letter2 in VOWELS) and 
            (letter1 == letter2)):
            
            vowel_once_count += 1

    if vowel_once_count == 1:
        vowels_once.append(letter1)

print()
print(f"Number of vowels: {vowel_count}")
print(f"List of vowels that appear only once: {vowels_once}")
print(f"Number of consonants: {consonants_count}")
