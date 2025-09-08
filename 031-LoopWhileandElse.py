# Loop - While and Else 

# num = 1 

# while num < 10 :
#     num +=1
#     print("Hello world")

# while False :
#     print("hello world")

# Exercise 1 

# my_friend = ["Ahmed","Mohamed","Mona","Nada","Younes"]
# num= 0
# while num <len(my_friend):
#     print(my_friend [num])
#     num+=1
   
# Exercise 2 

# my_friend = []

# x = int(input("how many fiends : "))
# status = 1

# while status <= x :
#     name_friend = input("please enter your friend : ")
#     my_friend.append(name_friend)
#     status+=1
# print(my_friend)

# Exercise 2   Password Guess
  
tries = 4
main_password = "Ahmed@333"


while tries >0:

    password =input("enter a password : ").strip().capitalize()
    tries -=1
    
    if password == "Ahmed@333":
        print("correct password")
        tries =0

 


        