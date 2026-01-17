#to find greatest of three numbers entered by users

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the three number"))

if(num1>=num2 & num1>=num3):
    greatest= num1
elif(num2>=num3):
    greatest= num2
else:
    greatest=num3

print("The grreatest number is", greatest)
