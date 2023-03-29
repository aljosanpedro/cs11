L = [5,3,1,2]

while True:
    swap = False
    
    for i in range(len(L)):
        if (i < len(L)-1) and (L[i] > L[i+1]):
            L[i],L[i+1] = L[i+1],L[i]
            swap = True
                
    if not swap:
        break

print(L) 
        