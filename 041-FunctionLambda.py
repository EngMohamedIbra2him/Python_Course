#  Function Lambda

def function_name(name): print(f"Hello {name}") 

say_hello = lambda name : print(f"Hello {name}")

function_name("mohamed")
print(function_name.__name__)
say_hello("ahmed")
print(say_hello.__name__)