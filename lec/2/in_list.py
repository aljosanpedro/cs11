L = [1,2,3,4,5]
print(f"List: {L}\n")

n = int(input("Number to check: "))

in_list = False


for i in range(len(L)):
    if n == L[i]:
        in_list = True
        break
        
        
print("\nElement in list:", in_list)

if in_list:
    print("Index in list:", i, '\n')
        