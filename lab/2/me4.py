h = int(input("Arrow Height: "))


for i in range(1,h+1):
    row = "*"
    row *= i
    print(row)

for i in range(h,1,-1):
    row = "*"
    row *= i
    print(row)
