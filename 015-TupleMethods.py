# Tuple is an Immutable Sequence Object

# print(type(tuple([1,2,3])))

my_tuple = ("mohamed","ahmed","ali","mando")
print(my_tuple[1:3])
# my_tuple[1]="Mona"  # error Immutable Item 
print(my_tuple)

# len()
print(len(my_tuple))

# tuple concatenation 
tuple1 = (2,4,8)
tuple2 = (1,3,9)
print(tuple1+ tuple2)

# List , Tuple & string Repeat 
list1 = [1,2,3,4]
tuple4 = (1,2,3,4)
my_string= ("ahmed","mohamed")
print(list1*2)
print(tuple4*2)
print(my_string*2)

# count()
my_count_tuple = (1,1,2,3,4,5)
print(my_count_tuple.count(1))

# index()
my_index_tuple = ("ahmed","ali","khaled")
print(my_index_tuple.index("ahmed"))

# destruct()
my_destruct_tuple = ("A","B","C")
x , y ,z =my_destruct_tuple
print(x,y,z)
