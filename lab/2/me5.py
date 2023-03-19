A = int(input())
B = int(input())


for i in range(A,B+1,1):
    result = ""
    
    
    if i % 3 == 0:
        result += "FIZZ"
    if i % 5 == 0:
        result += "BUZZ"
        
    if result == "":
        result = i
    
    
    print(result)
