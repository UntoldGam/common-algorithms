# order can have two possible values, Asc (ascending) and Des (descending)
from ...functions import typeCheck
def run(dataSet, order):
    # sorting goes here
    newDataSet = []
    sortedData = []
    for index, currentItem in dataSet.enumerate():
        nextItem = dataSet[index + 1]
        # only supports numbers for now
        if typeCheck(currentItem) == True and typeCheck(nextItem) == True:
            if currentItem > nextItem:
                newDataSet[index] = nextItem
                newDataSet[index + 1] = currentItem
            else:
                continue # no swaps made as items equal or [current < next]
    if order == "Des": # Biggest to Smallest
        sortedData = newDataSet.reverse()
    else: # Smallest to Biggest
        sortedData = newDataSet
    return [True, sortedData, False] # [Sorted, sortedData, Error]