# VARS
A = [2,2,3,8,5,6,6]
words = "My name is Dumbledore"
s1 = "If anything can go wrong, it will go wrong"


# LIST METHODS

# Add Elems
A.append(7)

A.insert(2,10)
A.insert(10,10)
A.insert(-1,1)
    # if i beyond len, inserts at end
    # i = -1, inserts at 2nd to last (i-1)

# Remove Elems
A.remove(10)
    # error if elem not in list
    
A.pop() # removes last
A.pop(2) # removes elem at index
x = A.pop(1) # pop returns what it removed

A.clear() # removes all elems in list

# Get Elems
A.index(8) # finds elem, returns index
A.index(14,2,9) # find 14, from index 2, until index 9

A.count(2)

# Sort
A.sort()
A.sort(reverse=True)
