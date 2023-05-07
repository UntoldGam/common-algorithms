from os import listdir, path

checkName = lambda x: x == '__pycache__' or x == "__init__.py"

ALG_DIR = "algorithms/"
ALG_TYPES = [category for category in listdir(ALG_DIR) if not checkName(category)]

def _doesAlgorithmExist(category, name):
    algorithms = getAlgorithms(category)
    #print(listdir(f"{ALG_DIR}{category}"))
    #print(algorithms)
    #print(name in algorithms)
    return name in algorithms
    #print(doesExist)
    #return doesExist

def _getAlgFunction(category, file):
    name = file.split('.py')[0]
    package = "algorithms"
    """
    imported = __import__(f"{package}.{category}.{name}")
    print(bubble.run())
    print(imported)
    #print(imported.run())
    """
    imp = getattr(__import__(f"{package}.{category}", fromlist=[name]), name)
    #print(imp.run())
    return imp.run

def getCategories():
    return ALG_TYPES

def getAlgorithms(category):
    return [algorithm.split('.py')[0] for algorithm in listdir(f"{ALG_DIR}{category}") if not checkName(algorithm)]

def storeAlgorithms(debug):
    #print("Creating algorithm dictionary")
    for category in listdir(ALG_DIR):
        if checkName(category):
            continue
        algorithms[category] = {}
        #print(algorithms, category)
        for algorithm in listdir(f"{ALG_DIR}{category}"):
            if checkName(algorithm):
                continue
            #print(algorithm)
            
def getAlgorithm(category, name):
    category = category.capitalize()
    name = name.capitalize()
    if category in ALG_TYPES:
        if _doesAlgorithmExist(category, name):
            return _getAlgFunction(category, name)
        else:
            return False
    else:
        return False