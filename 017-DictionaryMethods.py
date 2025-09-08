# Dictionary is an ordered Object

# Syntax => my_Dict = {key1:value1,key2:value2,key3:value3}

user = {
    "name": "mohamed",
    "age": 26,
    "skills" : {"python","html","c++","sql","linux"},
    "country": "Egypt"
}

# index()
print(user)
print(user["name"])
print(user["skills"])

# get()
print(user.get("age"))

# keys()
print(user.keys())

# items()
print(user.items())

# Two Dimension Dictionary
lang = {
    "one":{
        "name":"python",
        "rating":3.2
    },
    "two":{
        "name":"javascript",
        "rating":3.4
    },
     "three":{
        "name":"linux",
        "rating":3.5
    }
}

print(lang.keys())
print(lang.items())
print(lang["one"]["name"])
print(lang["two"]["rating"])
print(lang["three"]["name"])
print(len(lang["one"]))

# Concatenate Two Dictionary 
# all_dict = user + lang  #error 
all_dict = {"one": user,
            "two" :lang 
            }
print(all_dict.items())

# clear()
my_dict = {"name":"mohamed",
           "age":26}
# print(my_dict.clear())

# Update()
my_dict ["Title"] = "software developer"
print(my_dict)
my_dict.update({'Title':"software developer"})
print(my_dict)

# copy()
my_copy = {"one":"mohamed",
           "two":"ahmed"}
b= my_copy.copy()
print(b)

# fromkeys()
x = ("mohamed","ahmed","ali")
y = "x"
print(dict.fromkeys(x,y))