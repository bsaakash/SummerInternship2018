"""Write a python function to write to files. This function should take as input a list of numbers, find the length
of the input list of numbers, and write each entry in the list to a separate text file named 'File_n.txt', where 'n'
 stands for the position in the list of the number being written to the file, i.e., if the list has a length of 150,
 there should be 150 text files named 'File_1.txt', 'File_2.txt', etc., each containing the corresponding entry from
  the list."""
number = "f"
numList = []
while number != "":
    print("Enter a number. (Enter nothing if you would like the list to stop.)")
    number = input()
    if number !="":
        numList.append(number)
for i in range(len(numList)):
    file = open("C:\\Users\\gkim68\\Documents\\PracticeFiles\\File_"+str(i+1)+".txt", "w")
    file.write(numList[i])
    file.close()
