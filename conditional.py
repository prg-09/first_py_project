#conditional statement

marks= float(input("Enter the marks obtained"))
if(marks >= 90):
    print("Grade A")
elif(90>marks>= 80):
    print("Grade B")
elif(80>marks >= 70):
    print("Grade C")
elif(70>marks):
    print("Grade D")
else:
    print("invalid marks")

