while True:
    positive_integers = int(input("Input [Positive integer]: "))
    
    if positive_integers <= 0:
        print("Invalid input. Need a positive integer.")    
        continue
    
    break


sum = 0
positive_integers
for integer in range(1,positive_integers+1,1):
    sum += integer
    

print(f"Sum of first {positive_integers} positive integers: {sum}")
