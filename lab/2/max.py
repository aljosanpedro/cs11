L = []

n = int(input("How long is the list?: "))

for i in range(n):
    l = int(input(f"Item {i+1}: "))
    L.append(l)
    

max = 0

for x in L:
    if x > max:
        max = x

print("Max:", max)
