#  Iterable Vs Iterator

# Iterable is a Oject contain data can be iterated Upon
# Example (string ,list,set,Tuple,dictionary)

# Iterator is a oject used to Iterate over a iterable object by using next() method
# you can generate iterator from iterable when using iter() method

my_strig = "Mohamed"
my_list = [1,2,3,4,5,6,10]
num=10            # 'int' object is not iterable

for i in my_strig:
    print(i,end=" ")

print("\n")

for i in my_list:
    print(i,end=" ")
    
print("\n")

# for i in num:         # 'int' object is not iterable
#     print(i,end=" ")

my_iterator = iter(my_strig)
# print(next(my_strig))   #'str' object is not an iterator

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

