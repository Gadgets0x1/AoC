import string

def charValue(v: str) -> int:
    if(v.islower()):
        lower = list(string.ascii_lowercase)
        value = (lower.index(v))+1 
    else:
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

def groupBadge(groups: list) -> str :
    badgeInSet = set(groups[0]) & set(groups[1]) & set(groups[2])
    badgeCharacter = [str(i) for i in badgeInSet][0]
    return badgeCharacter

with open('./data.txt', 'r') as d:
    data = d.read().splitlines()
    rucksackSum = 0
    badgeSum = 0
    badgeGroupList = []
    for items in data:
        #----First
        rucksack = splitSack(items)
        itemType = getDubblet(rucksack)
        rucksackSum += charValue(itemType)
        #----

        #----Second
        badgeGroupList.append(items)
        if(len(badgeGroupList) % 3 == 0):
            badge = groupBadge(badgeGroupList)
            badgeSum += charValue(badge)
            badgeGroupList.clear()


        #----
    print(rucksackSum)
    print(badgeSum)