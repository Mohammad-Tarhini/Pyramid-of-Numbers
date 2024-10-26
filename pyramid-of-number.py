#Pyramid of Numbers
#Write a Python program that prompts the user for a number, x, and displays a pyramid of numbers. Each row in the pyramid should contain increasing numbers, starting from 1 up to x. 
x=int(input("please enter a number"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print("")
