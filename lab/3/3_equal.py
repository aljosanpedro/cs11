n = int(input("How many elements in the list?: "))

L = []
for i in range(n):
    L.append(input(f"Element #{i+1}: "))


same = True
for i in range(len(L)):
    if (i < len(L)-1) and (L[i] != L[i+1]):
        same = False


print("Are all elements in the list the same?:", same)
