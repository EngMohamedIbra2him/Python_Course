# Calculate Age Advanced Version

age = int(input("please enter your age : "))
print("enter the unit month , days or hours ")
unit = input("the unit is : ").strip().lower()


if unit == "m" or unit == "d" or unit == "h":
    if unit == "m":
        print(f"your age per months is :  {age*12} months") 

    elif unit == "d":
        print(f"your age per months is :  {age*12*30} days") 

    elif unit == "h":
        print(f"your age per months is :  {age*12*30*60} hours") 
else :
    print(f"this is an Invaild {unit} ")