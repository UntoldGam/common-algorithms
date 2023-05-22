# order can have two possible values, Asc (ascending) and Des (descending)
from ...functions import typeCheck
def merge(leftData, rightData):
    mergedItems = []
    leftLength, rightLength = len(leftData), len(rightData)
    leftIndex, rightIndex = 0, 0
    while leftIndex < leftLength and rightIndex < rightLength:
        currentItemLeft = leftData[leftIndex]
        currentItemRight = rightData[rightIndex]
        if typeCheck(currentItemLeft) == True and typeCheck(currentItemRight) == True:
            if currentItemLeft > currentItemRight:
                mergedItems.append(currentItemLeft)
                leftIndex += 1
            elif currentItemLeft < currentItemRight:
                mergedItems.append(currentItemRight)
                rightIndex += 1
    while leftIndex < leftLength:
        mergedItems.append(leftData[leftIndex])
        leftIndex += 1
    while rightIndex < rightLength:
        mergedItems.append(rightData[rightIndex])
        rightIndex += 1
    return mergedItems

def run(dataSet, order, r=None): 
    # dataSet = data to sort
    # order = "Asc"ending or "Des"cending
    # r = recursion? or final return 
    sortedData = []
    dataSet_length = len(dataSet)
    midpoint = (dataSet_length - 1) // 2 # perform Floor or Integer Division
    left_half = dataSet[0:midpoint+1] # Create left half list
    right_half = dataSet[midpoint+1:dataSet_length] # Create right half list

    left_half = run(left_half, order, True)
    right_half = run(right_half, order, True)

    mergedItems = merge(left_half,right_half)
    if r: 
        return
    else:
        if order == "Des": # Biggest to Smallest
            sortedData = mergedItems.reverse()
        else: # Smallest to Biggest
            sortedData = mergedItems
        return [True, sortedData, False] # [Sorted, sortedData, Error]