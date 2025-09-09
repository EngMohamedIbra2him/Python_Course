# Function Recursion

# def name (x):
    
#     return x +"ali" +"ahmed"

# print(name("mohamed"))

def clean_world (word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return clean_world(word[1:])
    return word[0] + clean_world(word[1:])

print(clean_world("wwworrrrdd"))

