# For Nested Loop

people = ["ahmed","mohamed","ali","mona"]

skills = {
"html":"90%",
"css":"80%",
"python":"70%",
"sql":"60%"
}


for i in people :
    print (f"{i}’s skills are : ")

    for j in skills:
        print(f"{j} .......{skills[j]}")