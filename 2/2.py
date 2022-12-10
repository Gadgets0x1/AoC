#(AX) Rock     1 (Z)Scissor 3 = 4
#(BY) Paper    2 (X)Rock    1 = 3
#(CZ) Scissors 3 (Y)Paper   2 = 5

# X  lose, 
# Y  draw,
# Z  win.

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
        playerTwo = player[2]
        t = t + totalScore(gameRound(playerOne,playerTwo),shapeScore(playerTwo))
    print(t)
    p.close()