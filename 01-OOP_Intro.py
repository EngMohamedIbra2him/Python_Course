# OOP Part 1 - Intro

# Class is the templete for creating objects [Object Constructor | BluePrint]
# Car is a class can you create many of cars from it

# class members :

#     def __init__(selfme):
#         print("New Member")


# member_one = members()
# print(dir(members))
# print(dir(member_one.__class__))

class members :
    def __init__(self,first_name):
        self.name = "mohamed"
        self.first_name = first_name
        self.age = 26

member_one = members("mohamed")
member_two = members("ahmed")
member_three = members("ali")

print(member_one.name)
print(member_two.name)
print(member_three.name)

print(member_one.first_name)
print(member_two.first_name)
print(member_three.first_name)