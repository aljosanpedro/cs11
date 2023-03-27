def main():
    print(convert([1,2,3]))
    
    
def convert(numbers):
    # Method 1: Map
    # map applies a fxn name (no parentheses) to an iterable
    return list(map(str(), numbers))

    # Method 2: List Comprehension
    # don't forget to enclose in list!
    # return [str(number) for number in numbers]
    
    
main()
