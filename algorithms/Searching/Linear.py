def run(dataSet, searchQuery):
    isFound = False
    for index, item in enumerate(dataSet):
        if item == searchQuery:
            isFound = True
            return [True, index] # [isFound, queryIndex, Error]
        else:
            continue
    return [False, False, False]