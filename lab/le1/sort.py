L = [5,9,2,3,10]

print(L)
print()

for i in range(len(L)):
    for j in range(i+1, len(L)):
        if L[j] > L[i]:
            print(f"{L[j]} > {L[i]}")
            L[i],L[j] = L[j],L[i]
            print(f"{L[i]} => {L[j]}, {L[j]} => {L[i]}")
            print(L)
            print()
    
    print(f"New List: {L}\n")
    print()
    