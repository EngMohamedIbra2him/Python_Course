# Function Scope

# x = 1    # Global Scope

def one():
    global x
    x=10
    print(f"x value is : {x}")

def two():
    # x=20
    print(f"x value is : {x}")

# print(x)
one()
two()
