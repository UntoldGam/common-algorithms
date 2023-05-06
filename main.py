from algorithmStore import getAlgorithm,storeAlgorithms,getCategories,getAlgorithms
from time import time,sleep
import re
from re import search
testData = [1,5,6,7,8,9]
testQuery = 200
categories = getCategories()
debug = True
numberCheck = lambda text: re.search("^\d*$", text)

def formatSearchResult(isFound, queryIndex, query):
    queryRes = f'{query} was found at index {queryIndex}' if isFound else f'{query} was not found'
    return queryRes + "\n"
    
def formatSortResult(isSorted, sortedData, originalData):
    sortRes = f'Original: {originalData}\nSorted: {sortedData}' if isSorted == True else 'Data was not sorted'
    return sortRes + "\n"

if __name__ == "__main__":
    category = "Searching" if debug else input(f"What type of algorithm would you like to use? \nValid Inputs: {categories} \n") 
    if category in categories:
        algorithm = "Linear" if debug else input(f"What is the name of the algorithm you would you like to use? \nValid Inputs: {getAlgorithms(category)} \n")
        runAlgorithm = getAlgorithm(category, algorithm)
        start_time = time()
        end_time = None
        dataSet = input(f"Please input the data you wish to use, each item should be seperated by commas: \nExample: 1,2,3 or q,a,e,c \n")
        newDataSet = []
        for item in dataSet.split(','):
            if numberCheck(item) != None:
                #print(item, "is a number")
                item = int(item)
            newDataSet.append(item)
        if category == "Searching":
            query = input("What item would you like to search for? ")
            r = runAlgorithm(newDataSet, query)
            end_time = time() - start_time
            isFound, queryIndex = r[0],r[1]
            message = formatSearchResult(isFound, queryIndex, query)
        elif category == "Sorting":
            order = input("What order would you like the data to be sorted into? ")
            r = runAlgorithm(newDataSet, order)
            end_time = time() - start_time
            isSorted, sortedData = r[0],r[1]
            message = formatSortResult(isSorted, sortedData, originalData)
        print(message, f"\nAlgorithm finished in {round(end_time, 2)}s.", end="\n")
        