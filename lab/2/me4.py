A = int(input())
B = int(input())
    
odds, evens = 0, []
    
    
for i in range(A,B+1,1):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds += 1
        
        
    print(i)
    
print("List of even numbers:", evens)
print("Number of odd numbers:", odds)
    