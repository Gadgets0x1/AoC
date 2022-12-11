import string

def lowerCaseValue(v: str) -> int:
    lower = list(string.ascii_lowercase)
    value = (lower.index(v))+1
    return value

def upperCaseValue(v: str) -> int:
    upper = list(string.ascii_uppercase)
    value = (upper.index(v))+27
    return value

def splitSack(rucksackItems: list) -> list:
    firstHalf = int((len(rucksackItems)-1)/2)
    secondHalf = int((len(rucksackItems))/2)
    ruck = rucksackItems[0:firstHalf], rucksackItems[secondHalf:]
    return ruck

def getDubblet(rucksack: list)-> str:
    char = set(rucksack[0]).intersection(rucksack[1])
    if(len(char) != 0):
        character = [str(i) for i in char]
        return character[0]
    else:
        return 0

#ta ut dubbleter de har ett värde

with open('./data.txt', 'r') as d:
    data = d.read().splitlines()
    rsum = 0
    for items in data:
        rucksack = splitSack(items)
        char = getDubblet(rucksack)
        if(char!=0):
            if(char.islower()):
                rsum = rsum + lowerCaseValue(char)
            else:
                rsum = rsum + upperCaseValue(char)
    
    print(rsum)