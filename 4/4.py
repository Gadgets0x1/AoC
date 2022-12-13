def sR(r: list) -> list:
    r = r.split('-')
    r1 = int(r[0])
    r2 = int(r[1]) + 1
    rlist = list(range(r1,r2))
    #listrange(sR(overLappingTasks[1]))
    return rlist

def overLappingTasks(overLappingTasks: list) -> int:
    firstList=sR(overLappingTasks[0])
    secondList=sR(overLappingTasks[1])
    if(len(firstList) < 2):
        third = firstList
    else:
        third=range(firstList[0], (firstList[-1]+1))

    if(len(secondList) < 2):
        fourth = secondList
    else:
        fourth=range(secondList[0], (secondList[-1]+1))
        
    fullRange= set(fourth).issubset(set(third)) or set(third).issubset(set(fourth))
    someOfTheRange = set(firstList).intersection(set(secondList))
 
    if fullRange: #first task
    #if someOfTheRange: #second task
        return 1
    else:
        return 0

def splitTask(task: list) -> list:
    twoTask = task.split(',')
    return twoTask

with open('./data.txt', 'r') as d:
    data = d.read().splitlines()
    count=0

    for tasks in data:
        taskList = splitTask(tasks)
        count += overLappingTasks(taskList)

    print(count)