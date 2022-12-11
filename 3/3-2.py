import string

def charValue(v: str) -> int:
    if(v.islower()):
        lower = list(string.ascii_lowercase)
        value = (lower.index(v))+1 
    else:
        upper = list(string.ascii_uppercase)
        value = (upper.index(v))+27
    
    return value

def upperCaseValue(v: str) -> int:
    upper = list(string.ascii_uppercase)
    value = (upper.index(v))+27
    return value

def splitSack(rucksackItems: list) -> list:
    half = int((len(rucksackItems))/2)
    ruck = rucksackItems[0:half], rucksackItems[half:]
    return ruck

def getDubblet(rucksack: list)-> str:
    char = set(rucksack[0]).intersection(rucksack[1])
    character = [str(i) for i in char][0]
    return character

def groupBadge(groups: list) -> int :
    badgeInSet = set(groups[0]) & set(groups[1]) & set(groups[2])
    badgeStr = [str(i) for i in badgeInSet][0]
    return badgeStr

with open('./data.txt', 'r') as d:
    data = d.read().splitlines()
    rsum = 0
    badgeGroupList = []
    bsum = 0
    for items in data:
        #----First
        rucksack = splitSack(items)
        char = getDubblet(rucksack)
        rsum = rsum + charValue(char)
        #----

        #----Second
        badgeGroupList.append(items)
        if(len(badgeGroupList) % 3 == 0):
            badge = groupBadge(badgeGroupList)
            bsum = bsum + charValue(badge)
            badgeGroupList.clear()


        #----
    print(rsum)
    print(bsum)