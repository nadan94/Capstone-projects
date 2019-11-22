#Introduction to programming, Task 12
#Capstone project 1
#Nadan Chetty, 2019/02/12
#Description:
#This program will create an investment calculator to calculate the users interest

import math

#initializing simpleInt and compoundInt
simpleInt = 0
compoundInt = 0

#request users input
P = float(input("Amount being deposited :"))
i = int(input("Interest rate :"))
t = int(input("Number of years :"))
interest = input("Simple/Compound? :").upper()

#Determining interest depending on users input then adding the interest to the principal deposit
if(interest == "SIMPLE"):
    simpleInt += P * (1 + (i / 100) * t)
    print(simpleInt)
elif(interest == "COMPOUND"):
    compoundInt += P * math.pow((1 + (i / 100)), t)
    print(compoundInt)
else:
    print("Invalid input")


