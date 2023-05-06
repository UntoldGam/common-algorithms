# order can have two possible values, Asc (ascending) and Des (descending)
def run(dataSet, order):
    # sorting goes here
    if order == "Des":
        sortedData = dataSet.reverse()
    else:
        sortedData = dataSet
    return [True, sortedData, False] # [Sorted, sortedData, Error]