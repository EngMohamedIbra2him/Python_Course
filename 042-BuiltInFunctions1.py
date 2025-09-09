# Built In Functions part one

# all()
my_list = [1,2,3,4,5,6,7,8,9,10]

if all(my_list):
    print("all element is Ture")
else :
    print("all element are false")

# any()

if any(my_list):
    print("there is an element is true")
else :
    print("all elemeny are false")

# bin()
x=22
print(bin(x))

# id()
a=12
b=13
print(id(a))
print(id(b))