def main():
    print(largest_difference([1,2,3]))
    
    
def largest_difference(numbers):
    biggest_number = max(numbers)
    smallest_number = min(numbers)
    
    largest_difference = biggest_number - smallest_number

    return largest_difference
    

main()
