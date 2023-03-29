A = [61,5,18,2,50,3]
B = []

for j in range(2,len(A)):
    key = A[j]
    B.append(key)
    i = j - 1
    
    while (i > 0) and (A[i] > key):
        A[i+1] = A[i]
        i -= 1
    
    A[i+1] = key
    
print(B)