ROCK, PAPER, SCISSORS = "rock", "paper", "scissors"
OPTIONS = [ROCK, PAPER, SCISSORS]

score1, score2 = 0, 0

while True:
    bet1 = input("Player 1 [rock, paper, scissors]: ")
    bet2 = input("Player 2 [rock, paper, scissors]: ")
    
    if (not bet1 in OPTIONS) or (not bet2 in OPTIONS):
        print("Invalid input.\n")
        continue


    if bet1 == bet2:
        print("Draw!\n")
        continue
    
    if (((bet1 == ROCK) and (bet2 == SCISSORS))
        or
        ((bet1 == PAPER) and (bet2 == ROCK)) 
        or
        ((bet1 == SCISSORS) and (bet2 == PAPER))):
        
        score1 += 1 
        print("Player 1 Wins!")
    else:
        score2 += 1
        print("Player 2 Wins!")
        
        
    print(f"Score: {score1} - {score2}\n")    


    if (score1 >= 3) or (score2 >= 3):
        print("Game Over!\n")
        break
