from random import randint

file = open("words.txt", 'r')
words = file.read()
words = file.split('\n')

word_index = randint(0, len(words))
hidden_word = words[word_index]

file.close()
