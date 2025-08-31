# Lists Methods 

# Append()
my_friends = ["Ahmed","Mona","ali"]
my_od_friends = ["Mamdouh","rania"]
my_friends.append("Sherif")
my_friends.append(my_od_friends)
print(my_od_friends)
print(my_friends)

# Extend()
list1=[1,2,3,4]
list2=[5,6,7,8]
list1.extend(list2)
print(list1)

# remove()
my_list = [1,2,3,4,5,6,7,8,9,10,"Ali","mona","Ahmed"]
my_list.remove(1)
print(my_list)

# sort()
my_sort_list = [1,2,3,4,5,6,7,8,9,10]
my_sort_list.sort(reverse=True)
print(my_sort_list)

# reverse()
my_reversed_list = ["ali","mona","ahmed"]
my_reversed_list.reverse()
print(my_reversed_list)

# copy()
my_copy_list = [2,4,8]
new_copy=my_copy_list.copy()
print(new_copy)

# count()
my_count_list = [1,1,1,1,1,1,2,3,4,5]
print(my_count_list.count(1))

# index()
my_index_list = ["ali","mona","ahmed"]
print(my_index_list.index("mona"))

# insert()
my_insert_list = [1,2,3,4,5,6,7,8,9,10]
my_insert_list.insert(0,"Test")
print(my_insert_list)

# pop()
my_pop_list = [1,2,30,4,5,6]
print(my_pop_list.pop(2))