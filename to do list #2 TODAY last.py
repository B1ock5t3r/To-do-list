#Fabian Rodriguez
#1/24/24
#List
print("Welcome to the hero selecter!")
heroes=["Iron-man", "Captain America", "Spider-man","Thanos","Ronan" ]
#Menu that allows user to remove all items from list, list all items in alphabetical order, and prints the #of items
Menu = input("Type 1 to remove all items from list, type 2 to sort items in alphabetical order, type 3 to print the number of items ")
if Menu == "1":
    heroes.clear()
    print(heroes)
if Menu == "2":
    heroes.sort()
    print(heroes)
if Menu == "3":
    print(len("heroes"))

