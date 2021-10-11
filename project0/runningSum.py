def runningSum(num):
    for index, element in enumerate(num):
        if (index == 0):
            sumArray = [num[0]]
        else:
            sumArray.append(sumArray[index-1] + num[index])

    return (sumArray)

num = [1,2,3,4]
numSums = runningSum(num)
print(numSums)



