# Sorting only supports numbers, no strings
def typeCheck(item):
    if type(item) == int or type(item) == float:
        return True
    elif type(item) == str:
        return False