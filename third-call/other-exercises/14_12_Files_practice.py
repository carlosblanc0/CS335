'''
Tasks
URL: https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/14/section/12

WGU is providing additional practice exercises for all students. The best method of learning Python is to practice. This will also help you prepare for the assessment, which requires you to write code.

Note: Replit is highly recommended for these exercises. This ensures cross-platform compatibility and removes potential file system risks from bad code.

Below is a sample exercise. You should copy the entire code snippet into your Python editor. Your code should be placed in the area that says “student code goes here” highlighted in yellow. This is inside the function. When you run this entire code snippet, there are test cases below your code. Your output should match the expected output.

'''

import os

# Task 1
def getCurrentDirectory():
    return os.getcwd()

# expected output: /tmp
# if using PyFiddle.io otherwise it varies
print(getCurrentDirectory())

# Task 2
def getDirectoryName(fileName):
    return os.path.dirname(fileName)

# expected output: /var/www
print(getDirectoryName("/var/www/test.html"))
# expected output: /var/www/apple
print(getDirectoryName("/var/www/apple/test.html"))

# Task 3
def getFileName(fileName):
    return os.path.basename(fileName)

# expected output: test.html
print(getFileName("/var/www/test.html"))
# expected output: names.txt
print(getFileName("/var/www/apple/names.txt"))

# Task 4
def createFile(filename):
    with open(filename, 'w'):
        pass
    return os.path.exists(filename)

# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))

# Task 5
def printFiles(someDirectory):
    for file in os.listdir(someDirectory):
        print(file)

# expected output: main.py
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())

# Task 6
def whatIsIt(somePath):
    if os.path.isfile(somePath):
        return "FILE"
    elif os.path.isdir(somePath):
        return "DIRECTORY"
    else:
        return "NEITHER"

# expected output: DIRECTORY
print(whatIsIt(os.getcwd()))
# expected output: FILE
print(whatIsIt(os.listdir(os.getcwd())[0]))
# expected output: NEITHER
print(whatIsIt('apple.pie.123.txt'))

# Task 7
def printFileContents(filename):
    with open(filename, 'r') as file:
        print(file.read())

# expected output: Hello
with open("test.txt", 'w') as f:
    f.write("Hello")
printFileContents("test.txt")

# Task 8
def appendAndPrint(filename, newData):
    with open(filename, 'a') as file:
        file.write(newData)
    printFileContents(filename)

# expected output: Hello World
with open("test.txt", 'w') as f:
    f.write("Hello ")
appendAndPrint("test.txt", "World")
