# Practical Membership Control

admins = ["mohamed","ahmed","ali","mona","sherif","dalia"]

name = input("enter your name : ").strip()

if name in admins:
    print("you are admin")
    options=input("Do you want to delete or Update : ")
    
    if options == "delete":
        admins.remove(name)
    else :
        new_name = input("enter your a new name : ")
        admins[admins.index(name)] = new_name
        print("Well Done")

else:
    print("you are not admin")

print(admins)