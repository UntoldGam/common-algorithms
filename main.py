from algorithmStore import getAlgorithm,getCategories,getAlgorithms
from time import time
from re import search
testData = [1,5,6,7,8,9]
testQuery = 200
categories = getCategories()
debug = True

# lambda functions
numberCheck = lambda text: search("^\d*$", text)

formatEndTime = lambda end: f"\nAlgorithm finished in {round(end_time, 2)}s."
formatSearchResult = lambda isFound, index, query: f'{query} was found at index {index}' if isFound else f'{query} was not found' + "\n"
formatSortResult = lambda isSorted, sortedData, originalData: f'Original: {originalData}\nSorted: {sortedData}' if isSorted == True else 'Data was not sorted' + "\n"

# main code
if __name__ == "__main__":
    category = "Searching" if debug else input(f"What type of algorithm would you like to use? \nValid Inputs: {categories} \n") 
    if category in categories:
        algorithm = "Linear" if debug else input(f"What is the name of the algorithm you would you like to use? \nValid Inputs: {getAlgorithms(category)} \n")
        runAlgorithm = getAlgorithm(category, algorithm)

        dataSet = input(f"Please input the data you wish to use, each item should be seperated by commas: \nExample: 1,2,3 or q,a,e,c \n")
        newDataSet = []
        for item in dataSet.split(','):
            if numberCheck(item) != None:
                #print(item, "is a number")
                item = int(item)
            newDataSet.append(item)
        if category == "Searching":
            query = input("What item would you like to search for? ")
            start_time = time()
            result = runAlgorithm(newDataSet, query)
            end_time = start_time - time()
            isFound, queryIndex = rresult[0],result[1]
            message = formatSearchResult(isFound, queryIndex, query) + formatEndTime(end_time)
        elif category == "Sorting":
            order = input("What order would you like the data to be sorted into? ")
            result = runAlgorithm(newDataSet, order)
            end_time = start_time - time()
            isSorted, sortedData = result[0],result[1]
            message = formatSortResult(isSorted, sortedData, originalData) + formatEndTime(end_time)
        print(message, end="\n")
        