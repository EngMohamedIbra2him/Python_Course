# Loop Advanced Dictionary

# my_skills = {
#     'html':"85%",
#     'python':"90%",
#     'Cpp':"90%",
#     'Xml':"80%",
#     'Sql':"85%"
# }

# for  key , value  in my_skills.items() :
#     print(f"{key} .......{value}")

my_skills = {
    "mohamed":{
        "html":"88%",
        "python":"90%",
        "sql":"85%"}
        ,

    "ahmed":{
        "html":"85%",
        "python":"85%",
        "sql":"90%"
        }
}

for key , value in my_skills.items():
    print(f'{key}.....')

    for i , j in value.items() :
        print(f"{i} ......{j}")