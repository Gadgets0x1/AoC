#(AX) Rock     1 (Z)Scissor 3 = 4
#(BY) Paper    2 (X)Rock    1 = 3
#(CZ) Scissors 3 (Y)Paper   2 = 5

# X  lose, 0
# Y  draw, 3
# Z  win. 6

def gameRound(p1: str, p2: str) -> int:
    if( (p1 == 'A' and p2 == 'Z')or
        (p1 == 'B' and p2 == 'X')or
        (p1 == 'C' and p2 == 'Y')):
        return 0
    if( (p1 == 'A' and p2 == 'Y')or
        (p1 == 'B' and p2 == 'Z')or
        (p1 == 'C' and p2 == 'X')):
        return 6
    return 3

def stratRound(p1: str, p2: str) -> str:
    if(p1 == 'A'): #Rock(AX)
        if(p2 == 'Z'): #win
            return 'Y'

        if(p2 == 'X'): #lose
            return 'Z'

        if(p2 == 'Y'): #draw
            return 'X'

    if(p1 == 'B'): #Paper(BY) 
        if(p2 == 'Z'): #win
            return 'Z'

        if(p2 == 'X'): #lose
            return 'X'

        if(p2 == 'Y'): #draw
            return 'Y'

    if(p1 == 'C'): #Scissor(CZ)
        if(p2 == 'Z'): #win
            return 'X'

        if(p2 == 'X'): #lose
            return 'Y'

        if(p2 == 'Y'): #draw
            return 'Z'

def shapeScore(shape: str) -> int: 
    if(shape == "X"):
        return 1
    if(shape == "Y"):
        return 2
    if(shape == "Z"):
        return 3

def totalScore(shapeScore: int, outcomeScore: int) -> int:
    total = shapeScore + outcomeScore
    return total

with open('./game.txt', 'r') as p:
    players = p.read().splitlines()
    t=0
    for player in players:
        playerOne = player[0]
        playerTwo = stratRound( player[0], player[2])
        t = t + totalScore(gameRound(playerOne,playerTwo),shapeScore(playerTwo))
    print(t)
    p.close()