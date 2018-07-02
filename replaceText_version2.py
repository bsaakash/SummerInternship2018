"""Write a python function (similar to the previous function), which takes three inputs - 1 list of strings,
1 filename, and 1 list of numbers. The function should check to see if the list of strings and the list of numbers
 have the same length. If the length is not the same, it should display an error message and stop execution. If the
 list is of the same length, then this function searches for the first string (for e.g., 'var1') in the file and
 replaces all instances of '' with the first number in the list, and so on for all the entries in the lists.
 There should be no other changes to the file."""

import re
wordList = []
numList = []

def fileReplacement(words,numbers,fileName):
    file = open(fileName)
    fileData = str(file.read())
    file.close()
    newData = ""
    for i in range(len(words)):
        stringRegex = re.compile(words[i],re.I)
        try:
            stringRegex.search(fileData)
            newData = newData + fileData[0:fileData.index(words[i])] + str(numbers[i])
            fileData = fileData[(fileData.index(words[i]) + len(words[i])):]
        except TypeError:
            print("The word: "+words[i]+" was not found.")
    newData = newData + fileData
    file = open(fileName, "w")
    file.write(newData)
    file.close()

def inputList():
    word = "f"
    while word != "":
        print("Enter the string to replace. (Enter nothing if you would like the list to stop.)")
        word = input()
        if word != "":
            wordList.append(word)

    number = "f"
    while number != "":
        print("Enter the number to replace the string with. (Enter nothing if you would like the list to stop.)")
        number = input()
        if number != "":
            numList.append(number)
    return wordList, numList


print("Enter the File Name.")
name = input()
wList, nList = inputList()
while (len(nList) != len(wList)):
    print("The length of the words and number lists are not equal. Please enter them again.")
    wList, nList = inputList()
fileReplacement(wList,nList,name)
