""" Write a python function to find and replace text in a file. This function takes three inputs - 1 string,
1 filename, and 1 number. It searches for the input string in the file, enclosed within '< >' and replaces ''
 with the number passed as input. i.e., if the input string is 'var1', the filename is 'Input_File_1.txt', and the
 input number is 12.34, the function searches for and replaces all instances of '' in the file 'Input_File_1.txt'
 with 12.34. There should be no other changes to the file."""

import re

print("Enter the File Name.")
fileName = input()
print("Enter the string to replace.")
changeString = input()
print("Enter the number to replace the string with.")
replace = int(input())

file = open(fileName)
fileData = str(file.read())
file.close()
stringRegex = re.compile(r"<"+changeString+r">")
newData = ""
for instance in stringRegex.findall(fileData):
    newData= newData + fileData[0:fileData.index(instance)]+str(replace)
    fileData = fileData[(fileData.index(instance)+len(instance)):]
newData = newData + fileData
file = open(fileName,"w")
file.write(newData)
file.close()
