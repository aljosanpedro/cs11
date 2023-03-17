def main():
    h = int(input("Arrow Height: "))


    for i in range(1,h+1):
        print_row(i)
        
    for i in range(h,1,-1):
        print_row(i)
    
def print_row(i):
    row = "*"
    row *= i
    print(row)

main()