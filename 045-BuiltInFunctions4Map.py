# Built In Functions Part 4 Map

# Map(Function,Iterable)

def say_hello(name):
    return f"Hello {name}"

name = ["mohamed","ahmed","ali"]

say = map(say_hello,name)

print(type(say))
print(say)

for i in say:
    print(i)