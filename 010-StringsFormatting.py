# Strings Formatting

# place Holding 
# %s =>String
# %d =>Integre
# %f =>Foating

# First Way for String Formatting 

name ="mohamed"
age = 26
rank =9.5

print("my name is ",name)
print("my name is ",name,"mg age is ",age)
print("my name is ",name,"mg age is ",age,"my rank is ",rank)

print("my name is %s"%name)
print("my name is %s"%name , "my age is %d" %age)
print("my name is %s "%name, "mg age is %d "%age, "my rank is %f "%rank)       # Seperated Message 
print("my name is %s my age is %d my rank is %f "  %(name ,age, rank))     # Full Message 


# Second Way for String Formatting 

print("my name is {}".format(name))
print("my name is {} my age is {}".format(name,age))
print("my name is {} my age is {} my rank is {}".format(name,age,rank)) 

# Third Way for String Formatting (Best Practise)

print(f"my name is {name}")
print(f"my name is {name} my age is {age}")
print(f"my name is {name} my age is {age} my rank is {rank}") 