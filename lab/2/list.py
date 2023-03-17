L = [4,5,9,1,3,10]
sum = 0
size = len(L)

for i in L:
    sum += i
    
print(sum / size)

"""
print("Old List:", L)
for i in range(len(L)):
    if L[i] % 2 == 0:
        L[i] *= 2
print("New List", L)
"""
    