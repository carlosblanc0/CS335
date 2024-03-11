'''
URL: https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/10/section/10
Taks: WGU is providing additional practice exercises for all students. The best method of learning Python is to practice. This will also help you prepare for the assessment, which requires you to write code.

You may use a web-based version of Python such as Repl.It to complete the exercises. Just make sure you are using version 3 or greater. If you use a web-based Python environment, you can easily share code with course instructors if you need help. You may also use a local installation of Python.

Below is a sample exercise. You should copy the entire code snippet into your Python editor. Your code should be placed in the area that says “student code goes here” highlighted in yellow. This is inside the function. When you run this entire code snippet, there are test cases below your code. Your output should match the expected output.
'''

# Task 1
def printFirst(mystring, x):
    print(mystring[:x])

# Task 2
def getLast(mystring, x):
    return mystring[-x:]

# Task 3
def containsWGU(mystring):
    return 'WGU' in mystring

# Task 4
def printWords(mystring):
    words = mystring.split()
    print(words)

# Task 5
def combineWords(words):
    return ' '.join(words)

# Task 6
def replaceWGU(mystring):
    return mystring.replace('WGU', 'Western Governors University')

# Task 7
def removeWGU(mystring):
    words = mystring.split()
    if len(words) > 0 and words[0] != 'WGU':
        words.remove('WGU')
    return ' '.join(words)

# Task 8
def removeSpaces(string1, string2):
    return string1.rstrip() + string2.lstrip()

# Task 9
def displayHourlyRate(rate):
    print('${:.2f}'.format(rate))

# Task 10
def countUpper(mystring):
    return sum(1 for char in mystring if char.isupper())

# Test cases
printFirst('WGU College of IT', 3)      # Output: WGU
print(getLast('WGU College of IT', 2))   # Output: IT
print(containsWGU('WGU College of IT'))  # Output: True
printWords('WGU College of IT')          # Output: ['WGU', 'College', 'of', 'IT']
print(combineWords(['WGU', 'College', 'of', 'IT']))  # Output: WGU College of IT
print(replaceWGU('WGU Rocks'))            # Output: Western Governors University Rocks
print(removeWGU('WGU Rocks'))             # Output: WGU Rocks
print(removeSpaces('WGU Rocks    ', '  -You know it!'))  # Output: WGU Rocks-You know it!
displayHourlyRate(34.789123)              # Output: $34.79
print(countUpper('Welcome to WGU'))      # Output: 4
