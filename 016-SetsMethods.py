# Set is a Unordered Object

my_set1 = {"mohamed","ali",True}
print(my_set1)
# print(my_set1[1]) # error is not orderd

# Unique Items
my_set2 = {1,2,3,1} 
print(my_set2)

# clear()
my_set3 = {1,2,3,"ahmed"}
my_set3.clear()
print(my_set3)

# union()
my_union_set1 = (10,20,30)
my_union_set2 = (40,50,60)
# print(my_union_set1 | my_union_set2)

# add()
my_add_set = {1,2,3,4,5,10}
my_add_set.add(100)
print(my_add_set)

# copy()
my_copy_set = {1,2,3,4,5,100,200,300,400}
x= my_copy_set.copy()
print(x)

# remove()
my_remove_set = (1,2,3,100,500)
print(my_remove_set.remove(500))
