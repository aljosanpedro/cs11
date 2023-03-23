def main():
    print(mid("abc"))


def mid(string):
    if len(string) % 2 != 0:
        middle = int(len(string) / 2)
        string = string[middle]
    else:
        string = ""
    
    return string
    
    
main()