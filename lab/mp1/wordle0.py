# HEADER
"""
Name: Alejandre Jose "Aljo" San Pedro
Section: LEC/LAB 1
Submission Date: 4/20/23

Short Description:
- The program first gets a random 5-letter hidden word from a words file.

- Then it loops the player guessing the hidden word for some tries.
    - Guesses not in the words file will not count as guesses.
- Letters of valid guesses will be color-coded:
    - Red for letter not in word
    - Yellow for letter in word but wrong position
    - Green for letter in word and right position
- Players can use a lifeline (1 guess) to reveal a new green letter.
- For each guess, each word guessed up until then will be printed with corresponding colors.

- If the player guesses the word within the given number of tries:
    - The score will be the number of remaining guesses.
- If the player doesn't guess the word within the given number of tries:
    - The word will be revealed
    
- Note: guesses or hidden words with many of the same letter were not considered during coding
"""


# IMPORTS
from random import randint
from termcolor import colored

# VALUES
# Constants
MAX_GUESSES = 6
MAX_LIFELINES = 2

LETTER_NOT_IN_WORD_COLOR = "red"
LETTER_IN_WORD_COLOR = "blue"
MATCHING_LETTERS_COLOR = "green"

UNDERSCORES_COLOR = "white" # lifeline

# Variables
guesses_left = MAX_GUESSES # counting down to 0
lifelines_left = MAX_LIFELINES

guessed_words = []
matching_letters = [] # lifeline

did_win = None # not True/False; want to use None/not None as condition of stopping game


# INITIALIZATION
# Hidden Word
    # Words in a file are read, put in a list, and then 1 is picked randomly
file = open("words.txt", 'r')

words = file.read()
words = words.split('\n')

hidden_word_index = randint(0, len(words)-1)
hidden_word = words[hidden_word_index]

file.close()

# Start Messages
print("\nWORDLE\n")
print("GUESS THE 5-LETTER HIDDEN WORD!")
print("Enter \"lifeline\" for a hint at the cost of 1 guess\n")

# Uncomment next line for easier checking of win code:
# print(f"Hidden Word: {hidden_word}\n")


# GUESSES
while True:    
    # GUESS INPUT
    print(f"GUESSES LEFT : {guesses_left}")
    guess = input("Your Guess: ").strip().lower() # lowercase formatting
    
    hidden_word = "spoon"
    
    # CASE: NO GUESS
    # Observed that inputting nothing counted as a guess
        # my guess: a words list element is blank
    if guess == "":
        print("GUESS IS EMPTY!\n")
        continue
    
    # CASE: LIFELINE
        # Opted to stick to revealing 1 letter only even if 2nd/higher lifeline
    
    if guess == "lifeline":
        # Check if still have lifeline/s
        if lifelines_left == 0:
            print("NO MORE LIFELINES LEFT\n")
            continue
        
        # Placeholders for manipulation
        lifeline_word = hidden_word
        lifeline_print_text = "_____"
        
        lifeline_print_colors = []
        
        # Remove known matching letters from hidden word
        for letter in matching_letters:
            lifeline_word = lifeline_word.replace(letter, '')
        
        # Randomly pick 1 unknown matching letter
        lifeline_letter_index = randint(0, len(lifeline_word)-1)
        lifeline_letter = lifeline_word[lifeline_letter_index]
        
        # Add picked letter to characters
        # Find index of letter in hidden words
        hidden_letter_index = hidden_word.find(lifeline_letter)
        
        # Type conversion to change an index value of string
        lifeline_print_text = list(lifeline_print_text)
        lifeline_print_text[hidden_letter_index] = lifeline_letter        
        lifeline_print_text = ''.join(lifeline_print_text) # list -> string
        
        # Add picked letter to matching_letters
            # Avoids duplicate lifelines
        matching_letters.append(lifeline_letter)
        
        # Colors assignment
        for character in lifeline_print_text:
            if character == '_':
                lifeline_print_colors.append(UNDERSCORES_COLOR)
            else:
                lifeline_print_colors.append(MATCHING_LETTERS_COLOR)
        
        # Printing
            # Shortened iterable names for convenience since repetitive guesss
            # Planned to loop and apply same index to both iterables, but this was easier  
        t = lifeline_print_text
        c = lifeline_print_colors
        
        print(
            colored(t[0],c[0]),
            colored(t[1],c[1]),
            colored(t[2],c[2]),
            colored(t[3],c[3]),
            colored(t[4],c[4]),
        )
        
        # Track lifeline use
        lifelines_left -= 1
        guesses_left -= 1
        
        print(f"LIFELINES LEFT : {lifelines_left}\n")
        
        # Check if still have guesses
        if guesses_left == 0:
            did_win = False
            break
        
        continue
    
    # CASE: NOT IN WORDLIST
        # Placed this late because it applied to "lifeline"
    if guess not in words:
        print("WORD IS NOT IN WORDLIST!\n")
        continue
    
    # CASE: VALID WORD GUESS
        # No need for if statement identifier since all other cases were covered
    
    # Remember all guesses until current one
    guessed_word = guess # change name for logic
    guessed_words.append(guessed_word)
    
    # Check each guess up to current one
    for word in guessed_words:
        
        # Track colors per letter in current word
        word_print_colors = []
        
        for letter in word:
            # Letter not in word -> RED
            if letter not in hidden_word:
                word_print_colors.append(LETTER_NOT_IN_WORD_COLOR)
                continue # ensures next lines assume letter is in word
            
            # Letter in word -> Yellow or Green
            # Compare indeces of hidden & guessed words -> Green if match, Yellow if not
            
            # Letter Indeces
                # careful to not find using guessed word -> colors of current guess apply to old
            guessed_letter_index = word.find(letter)
            hidden_letter_index = hidden_word.find(letter)
            
            # YELLOW
            if not guessed_letter_index == hidden_letter_index:
                word_print_colors.append(LETTER_IN_WORD_COLOR)
                continue
            
            # GREEN
            word_print_colors.append(MATCHING_LETTERS_COLOR)
            
            if letter not in matching_letters:
                matching_letters.append(letter) # for lifeline
        
        # Print Colored Word
            # Same thought process with lifeline printing
        w = word # letter
        c = word_print_colors # color of letter
        
        print(
            colored(w[0],c[0]),
            colored(w[1],c[1]),
            colored(w[2],c[2]),
            colored(w[3],c[3]),
            colored(w[4],c[4]),
        )
    
    # POST-GUESS
    print()
    
    # Update guesses left
    guesses_left -= 1
    
    # Stop if win or lose
    if guessed_word == hidden_word:
        did_win = True
    elif guesses_left == 0: # used elif in case won on last guess
        did_win = False
    
    if not did_win is None:
        break
        

# RESULTS
print()

if did_win:
    print("CONGRATULATIONS! YOU HAVE GUESSED THE HIDDEN WORD!\n")
    score = guesses_left + 1 # +1 since guesses_left subtracted from when win
    print(f"YOUR SCORE : {score}")
else:
    print("YOU LOSE!\n")
    print(f"HIDDEN WORD : {hidden_word}")

print()
