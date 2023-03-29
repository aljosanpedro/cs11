money = int(input())

DENOMS = [1000, 500, 200, 100, 50, 20, 10, 5, 1]


for denom in DENOMS:
    denom_count = int(money / denom)
    money %= denom
    
    print(f"{denom_count} x {denom}")
    