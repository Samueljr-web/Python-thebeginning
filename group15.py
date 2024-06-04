# write a python program that takes two number and print the larger one


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

def HigherNumber(num1,num2):
    if (num1 > num2):
        print(num1)
    else:
       print("The highest number is " +str(num2)) 

HigherNumber(num1,num2)


