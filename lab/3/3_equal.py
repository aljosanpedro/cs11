elements = int(input("\nHow many elements in the list?: "))
print()

list = []
for element in range(elements):
    list.append(input(f"Element #{element+1}: "))


same = True
for element in range(elements):
    if element < len(list)-1:
        if list[element] != list[element+1]:
            same = False


print()
print("Are all elements in the list the same?:", same)
print()
