#to input three movies from users and list them
mov1 = input("Enter the name of first movie")
mov2 = input("Enter the name of second movie")
mov3 = input("Enter the name of third movie")
list = [mov1]
list.append(mov2)
list.append(mov3)
print(list)
print(type(list))
