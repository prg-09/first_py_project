#to check if the elements are in palindrome or not
first = input("Enter the first element of the list ")
second = input("Enter the second element of the list ")
third = input("Enter the third element of the list ")
list = [first, second, third]
copylist = list.copy()
copylist.reverse()
if(copylist == list):
    print("The elements are palindrome")
else:
    print("The elements are not palindrome")
