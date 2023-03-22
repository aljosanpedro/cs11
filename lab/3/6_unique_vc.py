VOWELS = "aeiou"
vowels_counts, consonants_counts = [[],[]], [[],[]]

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


for letter in word:
    if letter in VOWELS:
        if not letter in vowels_counts[0]:
            vowels_counts[0].append(letter)
            vowels_counts[1].append(1)
        else:
            vowel_index = vowels_counts[0].index(letter)
            vowels_counts[1][vowel_index] += 1
    else:
        if not letter in consonants_counts[0]:
            consonants_counts[0].append(letter)
            consonants_counts[1].append(1)
        else:
            consonant_index = consonants_counts[0].index(letter)
            consonants_counts[1][consonant_index] += 1


print("Vowels Counts:")
for v in range(len(vowels_counts[0])):
    print(f"{vowels_counts[0][v]} : {vowels_counts[1][v]}")
print()

print("Consonants Counts:")
for c in range(len(consonants_counts[0])):
    print(f"{consonants_counts[0][c]} : {consonants_counts[1][c]}") 
print()