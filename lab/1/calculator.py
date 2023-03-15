first = float(input())
second = float(input())
operator = input()

result = 0


# zero division error
if ((second == 0) and (operator == '/')):
    print("undefined")
else:
    """
    commands dict placed here bc values evaluate! (ex. first + second)
    -> actual zero div error possible if placed above check
    """
    commands = {
        '+' : first + second,
        '-' : first - second,
        '*' : first * second,
        '/' : first / second,
    }


    for command in commands:
        if operator == command:
            result = commands[command]    
    
    print(result)
    