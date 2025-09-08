# Membership Operators 

# In 
# not In

# string 
name = "mohamed"
print("a" in name )
print("h" in name )
print("D" in name )

# list
friends = ["ahmed","younes","mamdouh"]
print("younes" in friends)
print("ahmed" not in friends)
print("mamdouh" in friends)

# exercise 1 
country_names = ["egypt","ksa","kwuait"]
my_country = "egypt"

if my_country in country_names :
    print("your discount is 80%")