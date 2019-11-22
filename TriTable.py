#Introduction to programming, Task 15
#Capstone project 2
#Nadan Chetty, 2019/02/16
#Description:
#This program will create a multiplication pyramid

for x in range(1,10):
#range excludes last number (x + 1) will include it
    for y in range(1, x + 1):
        print (x * y, end=" ")
#The print "\n" function is for the appropriate line spacing
    print("\n")
        
        
        
