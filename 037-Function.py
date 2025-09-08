#  Function 

def function_name ():
   
    return "Hello world"
print(function_name())

def function_name ():
    name = input("please enter a name : ")
    return f"Hello {name.capitalize()}"

print(function_name())

#  Function Parameters And Arguments

def say_hello (name):
    return f"Hello {name.capitalize()}"

print(say_hello("mohamed"))
print(say_hello("ahmed"))

def add_func (n1,n2):
    if type(n1) != int or type(n2) != int :
        print("Intgre only")
    else :
        print(n1+n2)
    return "okay..."

print(add_func(10,20))
print(add_func(10,"mohamed"))

# Function Default Parameters

def say_hello(name= "Mohamed" ,age = "unkown" , country="Unkown"):
    print(f"Hello {name} your age is : {age} and your country is : {country}")

print(say_hello("mohamed",26,"egypt"))
print(say_hello("ahmed",28))
print(say_hello("Hossam"))
print(say_hello(age=28))

# Function Packing, Unpacking Arguments
 

