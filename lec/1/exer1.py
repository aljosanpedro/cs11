# gave up on this, idk xD

while True:
    n = int(input("Odd number greater than 2: "))
    
    if (n % 2 != 0) and (n > 2):
        break
    
flag = False


for i in range(2, int(n/2)): # ex. int(1.5) = 1, not rounded even if .5!
    print(f"{n} % {i} = {n % i}")
    if n % i != 0:
        flag = True
        print(f"{n} % {i} = {n % i}")
        break
   

print("Composite") if flag else print("Prime")
