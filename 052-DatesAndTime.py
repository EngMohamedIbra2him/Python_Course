# Date And Time Introduction

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print("#"*50)
print(datetime.datetime.min)
print(datetime.datetime.max)
print("#"*50)
print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)
print("#"*50)
print(datetime.time.min)
print(datetime.time.max)
print("#"*50)
print(datetime.datetime(1998,10,1))

# calculate an age 

date_of_birth = datetime.datetime(1998,10,1)
date_now =datetime.datetime.now()
my_age_now = date_now - date_of_birth

print(f"my age is {my_age_now.days}")
print(f"my age is {my_age_now.days/360} year ")
print("#"*50)


# Date And Time Format Date

my_birthday = datetime.datetime(1998,10,1)

print(my_birthday.strftime("%B"))
print(my_birthday.strftime("%A"))
print(my_birthday.strftime("%y"))
print(my_birthday.strftime("%d"))
print(my_birthday.strftime("%d  %B  %y"))


