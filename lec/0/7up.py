L = input("List [x,y,...,z]: ") # list as 1 string
L = L.split(sep=',') # list of chars

# convert chars to ints
for i in range(len(L)):
    L[i-1] = int(L[i-1])
    
n = len(L)
i = 0
total = 0

while True:
    if i != n:
        i += 1
        j = L[i-1]
        total += j
        
    else:
        print(total)
        
        r = total % 7
        if r == 0:
            print("7UP!")

        break
        