"""Write a python function which takes 3 inputs - 1 list of strings, 1 filename, and a matrix(lists of lists) of numbers.
The objective of this function is to use a template file and create input files for the models. The function
 first checks to see if the number of columns of the matrix is the same as the length of the list of strings.
  The filename is the name of a template file which contains the placeholders for the variables at different
  locations within the file, along with some other text i.e., strings such as ',', '', ...,'', where m is the
   length of the list, are dispersed within other text in the file. The function loops over the number of rows
of the input matrix of numbers, searches for the strings (which are in the list of input strings) in the template
file, and replaces them with the corresponding number from that row, and saves this file as 'File_n.inp', where 'n'
is the current row number."""

import re, os, numpy

#replaces the corresponding word and number in each location of the lists
def fileReplacement(words,numbers,fileData,userFormat,first):
    if (userFormat == "") or (userFormat[0:1]!="{:" and userFormat[len(userFormat)-1]!= "}"):
        userFormat = "{:.4E}" #only 5 significant digits

    for i in range(len(words)):
        stringRegex = re.compile(r"<"+words[i]+r">")
        count = 0;
        for string in stringRegex.findall(fileData):
            fileData = fileData[0:fileData.index(string)] + str(userFormat.format(float(numbers[i])))\
                       + fileData[(fileData.index(string) + len(string)):]
            count  += 1
        if first==0:
            print("Found: "+str(count)+" instances of word: "+words[i])
    return fileData

def check(matrix,words,fileName,newFolder,format):
    for i in range(len(matrix)):
        if (len(matrix[i]) != len(words)):
            print("The length of the words and number lists are not equal in column: " + str(
                i + 1) + ". Please enter them again.")
            break
        else:
            file = open(fileName)
            fileText = str(file.read())
            file.close()
            newText = fileReplacement(words, matrix[i], fileText,format,i)
            if not os.path.exists(newFolder):
                os.makedirs(newFolder)
            baseName = os.path.splitext(os.path.basename(fileName))
            file = open(os.path.join(newFolder,baseName[0]+"_"+"{0:05}".format(i+1)+baseName[1]), "w")
            file.write(newText)
            file.close()
    print(str(i + 1)+ " input files created for: "+ baseName[0]+baseName[1])


wordList2 = ["youngs_modulus", "yield_stress", "ultimate_stress"]
matrixList2 = numpy.random.rand(5,3)
name2 = "PracticeFiles\\beam_GMNIA.inp"
folder = "C:\\Users\\gkim68\\Documents\\NewFolder"
format = "{:.4E}" #ALL FORMATS SHOULD BE IN {:___}

check(matrixList2,wordList2,name2,folder,format)
