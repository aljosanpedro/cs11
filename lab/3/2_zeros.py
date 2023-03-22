while True:
    binary = input("Binary string [ex. 101001000]: ")
    valid = True

    for char in binary:
        if not char in "01":
            valid = False
            
    if not valid:
        print("Invalid input.")
        continue
    
    break
    

consec, largest_consec = 0,0

for i in range(len(binary)):
    if binary[i] == '0':
        consec += 1
    else:
        consec = 0
        
    if consec > largest_consec:
        largest_consec = consec
        index = i - largest_consec + 1
        

print("Index of first 0 in largest consecutive substring:", index, '\n')
