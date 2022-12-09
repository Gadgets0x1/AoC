with open('./elves', 'r') as f:
    elves={}
    calories=0
    largestCalories=0
    mostCalories={}
    count = 1
    for line in f:
        if(line.strip()):
            calories=calories+int(line.strip())
        else:
            if(calories > largestCalories):
                largestCalories = calories
                mostCalories["most"]=[count,calories]
            elves[count] = calories
            count=count+1
            calories = 0
    print(mostCalories)
