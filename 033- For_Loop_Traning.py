# Loop For Training

my_range = range(1,100)

# for i in my_range:
#     print(i)

my_dict = {
    'html':"85%",
    'python':"90%",
    'Cpp':"90%",
    'Xml':"80%",
    'Sql':"85%"
}

print(my_dict["html"])

for i in my_dict:
    print(f'my peogress in {i} is {my_dict[i]}')