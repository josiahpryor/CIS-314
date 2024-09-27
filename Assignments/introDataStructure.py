def main():
    #Creating data structures
    mySet = {1,2,3,4,5,6,7,8,9,10}
    myDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,
              'f':6, 'g':7, 'h':8, 'i':9, 'j':10}
    #Reverse order
    myDict = reverseData(myDict)

    #printing data structures
    print("Inital set:\n",mySet)
    print("Inital dictionary:\n",myDict)

    #Pick 3rd element
    printElement(mySet, 3)
    printElement(myDict, 3)

    #Add 11th element to end of structure
    myDict["k"] = 11
    print("Dictionary with 11th element added:\n",myDict)
    mySet.add(11)
    print("Set with 11th element added:\n",mySet)

    #Remove first element
    mySet.pop() #Since sets are unordered and the first element cannot be remove, a random value is removed instead
    print("A random element of mySet has been removed because it is unordered:\n", mySet)

    removeFirst(myDict)
    print("Dictionary with first element removed:\n", myDict)

    #Remove same element from both structures
    #This cannot be done since a dictionary is an ordered structure while a set is not


def removeFirst(myDict):
    myList = list(myDict.items())
    firstKey, firstValue = myList[0]
    del myDict[firstKey]

def printElement(dataStr, element):
    if isinstance(dataStr, dict):
        elementData = list(dataStr.items())[element-1]
        print("Element", element, "of the dict is:", elementData)
    else:
        elementData = (list(dataStr))[element-1]
        print("Element", element,"of the set is:", elementData)

def reverseData(dataStr):
    #Sets cannot be reversed because they are unordered

    myDict_Reversed = dict(reversed(list(dataStr.items())))
    return myDict_Reversed

if __name__ == "__main__":
    main()