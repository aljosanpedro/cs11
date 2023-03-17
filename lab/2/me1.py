A = int(input())
B = int(input())
    
evens = []
odds = 0
    
    
for i in range(A,B,1):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds += 1
       
        
print("Even numbers from A to B:", evens)
print("Number of odd numbers from A to B:", odds)
    