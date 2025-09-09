# Function Packing Unpacking Arguments
# *kWArg  this a typle 
# **KWArg this is a dictionary 

my_list = [1,2,3,4,5]

# print(my_list)
# print(*my_list)  # Unpacking
# ##################################################
# def my_func1(n1,n2,n3,n4):
#     people = [n1,n2,n3,n4]
#     for i in people:
#         print(i)
# my_func1("Html","css","python","cpp")
# ##################################################
# def my_func2(*people):
#     for i in people:
#         print(i)
# my_func2("Html","css","python","cpp","Js")
# ##################################################

# def show_skills(name , *skills):
#     print(f"Hello {name} your skills are :.....")
#     for i in skills :
#         print(i)

# show_skills("mohamed","python","linux","embedded system","cpp","xml")
# ##################################################

#  Function Packing Unpacking Keyword Arguments **kwargs
name = "Moahmed"

skills = ("html","css","python","js","cpp","sql")


skills_with_progress = {
    'html':"85%",
    'python':"90%",
    'Cpp':"90%",
    'Xml':"80%",
    'Sql':"85%"
}

def show_my_skills (name , *skills,**skills_with_progress):
    print(f"Hello {name} your skills is : ")
    skills_list =[]

    # for skill in skills:
    #     skill =list(skill)
        
    #     skills_list.append(skill)
    # print(skills_list)

    for key , value in skills_with_progress.items():
        print(f"my skill is {key} , and my progress os {value}")

show_my_skills(name,*skills,**skills_with_progress)