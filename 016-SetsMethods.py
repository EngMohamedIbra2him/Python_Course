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
# my_remove_set.remove(500)

# difference()
my_difference_set1 = {1,2,3,4,5}
my_difference_set2 = {1,2,3,"Mohamed"}
print(my_difference_set1.difference(my_difference_set2))
print(my_difference_set1)

# difference_update()
my_difference_set1 = {1,2,3,4,5}
my_difference_set2 = {1,2,3,"Mohamed"}
my_difference_set1.difference_update(my_difference_set2)
print(my_difference_set1)

# intersection()
my_intersection_set1 = {1,2,3,4,5}
my_intersection_set2= {1,2,3,"mohamed","ali",'ahmed'}
print(my_intersection_set1.intersection(my_intersection_set2))

# intersection_update()
my_intersection_set1 = {1,2,3,4,5}
my_intersection_set2= {1,2,"mohamed","ali",'ahmed'}
my_intersection_set1.intersection_update(my_intersection_set2)
print(my_intersection_set1)

# issuperset()
my_suberset1= {1,2,3,4,5,6,7,8,9,10}
my_suberset2= {1,10}
print(my_suberset1.issubset(my_suberset2))
print(my_suberset2.issubset(my_suberset1))

# issubset()
my_subset1= {1,2,4,5,6,7,8,9,10}
my_subset2= {1,10}
print(my_suberset1.issubset(my_subset2))



