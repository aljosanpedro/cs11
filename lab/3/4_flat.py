# Program description
print("\nThe program will ask you to input a 2D-list (ex. [[1,2],[3,4]])")
print("It will then flatten the 2D-list into a 1D-list (ex. [1,2,3,4])\n")

# No. of sublists
while True:
    sublists = float(input("How many sublists [positive integer]: "))
    
    if (sublists <= 0) or (not sublists.is_integer()):
        print("Invalid input.\n")
        continue

    sublists = int(sublists) # float -> int
    break
print()

# No. of elements per sublist
elements = []
for sublist in range(sublists):
    while True:
        sublist_elements = float(input(f"How many elements in sublist #{sublist+1}? [positive integer]: "))
    
        if (sublist_elements <= 0) or (not sublist_elements.is_integer()):
            print("Invalid input.\n")
            continue
        
        sublist_elements = int(sublist_elements) # float -> int
        elements.append(sublist_elements)
        break
print()

# Fill in the list with sublists
list_2d = []
for sublist in range(sublists):
    list_2d.append([])
    
    # Fill in the sublists with elements
    for element in range(elements[sublist]):
        temp_elem = input(f"Sublist #{sublist+1}, Element #{element+1}: ")
        list_2d[sublist].append(temp_elem)
    print()
    
# Unflattened list
print(f"Unflattened list: {list_2d}\n")


# Flatten list
list_flat = []

for sublist in range(sublists):
    for element in range(elements[sublist]):
        list_flat.append(list_2d[sublist][element])
        
print(f"Flattened list: {list_flat}\n")
