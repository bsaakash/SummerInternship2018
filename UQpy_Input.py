import sys
import matrixTable

index = sys.argv[1]
# index = 2
f = open("C:\\Users\\gkim68\\PycharmProjects\\PythonScripts\\SummerInternship2018\\ABAQUS_Model\\UQpy_Samples.txt")
line = f.readlines()
matrixList= [[float(line[index].strip())]]
wordList = ["youngs_modulus"] # TODO: this should come from UQpy
name = "C:\\Users\\gkim68\\PycharmProjects\\PythonScripts\\SummerInternship2018\\ABAQUS_Model\\LBA_beam.inp" # Template input file
folder = "C:\\Users\\gkim68\\PycharmProjects\\PythonScripts\\SummerInternship2018\\ABAQUS_Model"
format = "" # make this an optional argument

matrixTable.check(matrixList,wordList,name,folder,format,index)