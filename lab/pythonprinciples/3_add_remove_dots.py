def main():
    print(remove_dots(add_dots("test")))


def add_dots(word):
    word = '.'.join(word)
    
    return word


def remove_dots(word):
    word = word.replace('.','')
    
    return word

   
main()
