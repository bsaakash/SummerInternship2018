import sys
import matrixTable
import os

index = sys.argv[1]
#index = 0
fldr = os.getcwd()
fnm_samples = os.path.join(fldr,"UQpy_Samples.txt")
# f = open("C:\\Users\\gkim68\\PycharmProjects\\PythonScripts\\SummerInternship2018\\ABAQUS_Model\\UQpy_Samples.txt")
f = open(fnm_samples)
line = f.readlines()

print(index)
print(type(index))

# print(line[index].strip())
# type(line[index].strip())

matrixList = [[float(line[int(index.strip())])]]
#wordList = ["youngs_modulus"] # TODO: this should come from UQpy
wordList = ["thickness"] # TODO: this should come from UQpy
template_name = os.path.join(fldr,"LBA_beam.inp")
# name = "C:\\Users\\gkim68\\PycharmProjects\\PythonScripts\\SummerInternship2018\\ABAQUS_Model\\LBA_beam.inp" # Template input file
folder = fldr
# folder = "C:\\Users\\gkim68\\PycharmProjects\\PythonScripts\\SummerInternship2018\\ABAQUS_Model"
frmt = "" # make this an optional argument

matrixTable.check(matrixList,wordList,template_name,folder,frmt,index)