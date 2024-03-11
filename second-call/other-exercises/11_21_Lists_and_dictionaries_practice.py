'''
Tasks
URL: https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/11/section/21

WGU is providing additional practice exercises for all students. The best method of learning Python is to practice. This will also help you prepare for the assessment, which requires you to write code.

You may use a web-based version of Python such as PyFiddle, Repl.It, or PythonFiddle to complete the exercises. Just make sure you are using version 3 or greater. If you use a web-based Python environment, you can easily share code with course instructors if you need help. You may also use a local installation of Python.

Below is a sample exercise. You should copy the entire code snippet into your Python editor. Your code should be placed in the area that says "student code goes here" highlighted in yellow. This is inside the function. When you run this entire code snippet, there are test cases below your code. Your output should match the expected output.

'''

# Task 1
def getFirstTwo(mylist):
    return mylist[:2]

print(getFirstTwo([8,3,5,2,10]))
print(getFirstTwo([15,2,10,12]))

# Task 2
def getLastTwo(mylist):
    return mylist[-2:]

print(getLastTwo([8,3,5,2,10]))
print(getLastTwo([15,2,9,12]))

# Task 3
def addToEnd(mylist, num1):
    mylist.append(num1)
    return mylist

print(addToEnd([4,5,6], 7))
print(addToEnd([9,8,7], 6))

# Task 4
def addToFront(mylist, num1):
    mylist.insert(0, num1)
    return mylist

print(addToFront([4,5,6], 3))
print(addToFront([9,8,7], 10))

# Task 5
def getFirstTwoAndLastTwo(mylist):
    return mylist[:2] + mylist[-2:]

print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))

# Task 6
def removeFirst(mylist):
    mylist.pop(0)
    return mylist

print(removeFirst([6,7,8,9]))
print(removeFirst([1,2,3,4]))

# Task 7
def removeThird(mylist):
    mylist.pop(2)
    return mylist

print(removeThird([6,7,8,9]))
print(removeThird([1,2,3,4]))

# Task 8
def sortList(mylist, ascending):
    return sorted(mylist) if ascending else sorted(mylist, reverse=True)

print(sortList([19,4,33,12], True))
print(sortList([19,4,33,12], False))

# Task 9
def createDict(list1, list2):
    return dict(zip(list1, list2))

print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))

# Task 10
def findDictItem(mydict, key):
    return mydict.get(key, 'Not Found')

print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))

# Task 11
def removeDictItem(mydict, key):
    if key in mydict:
        del mydict[key]
    return mydict

print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))

# Task 12
def printDict(mydict):
    for key, value in mydict.items():
        print(f"{key}={value}")

printDict({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'})
printDict({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'})
