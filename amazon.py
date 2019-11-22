#Introduction to programming, Task 20
#Capstone project 3
#Nadan Chetty, 2019/02/22
#Description:
#This program will read from 'input.txt', calculate min, max and avg then write to 'output.txt'

#Opening the textfiles
inputTxtRead = open('input.txt', 'r+', encoding='utf-8-sig')
outputTxtWrite = open('output.txt', 'w')

#Splitting each new line
#Needed to use .read() because it will read row
content = inputTxtRead.read().split("\n")

for i in range(0,3):
    line = content[i].split(":")
    #Function to be performed
    lineFunc = line[0]
    #List of numbers(string list)
    lineNums = line[1].split(",")
    if lineFunc == "min":
        #Prints the min value
        outputTxtWrite.write("The min of {0} is {1}\n".format(lineNums, min(lineNums)))
    elif lineFunc == "max":
        outputTxtWrite.write("The max of {0} is {1}\n".format(lineNums, max(lineNums)))
    else:
        #casts string list to an integer list
        lineNums = list(map(int, lineNums))
        #Prints the average
        outputTxtWrite.write("The avg of {0} is {1}\n".format(lineNums, sum(lineNums)/len(lineNums)))
inputTxtRead.close()
outputTxtWrite.close()
