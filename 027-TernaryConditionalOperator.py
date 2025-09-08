# Ternary Conditional Operator

country = "egypt"

if country == "egypt": print(f"the weather of your {country} is 38")

elif country == "ksa":  print(f"the weather of your {country} is 40")

else : print("In vaild country ")

# short if
moive_rate = 18
age = 16

if age >moive_rate  :
    print("the moive is suaitable for you")
else:
    print("the moive is not suaitable for you")
    
# short if 
print("this moive is not good for you " if age < moive_rate else "moive is good for you")