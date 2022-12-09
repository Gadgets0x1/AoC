with open('./elves', 'r') as f:
    f = f.read().splitlines()
    calories = 0
    largestCalories = 0
    mostCaloriesDict = {}
    mostCaloriesList = []
    elvesList = []
    count = 1

    for calorie in f:
        if (calorie):
            calorie = int(calorie)
            calories = calories + calorie

            if (calories > largestCalories):
                largestCalories = calories
                mostCaloriesDict["most"] = [calories]
        else:
            elvesList.append(calories)
            count = count+1
            calories = 0

    print(mostCaloriesDict)
    elvesList.sort()
    topThree = (
        elvesList[len(elvesList)-1] +
        elvesList[len(elvesList)-2] +
        elvesList[len(elvesList)-3]
    )
    print(topThree)