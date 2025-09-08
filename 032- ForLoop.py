#  For Loop 


my_numbers = [1,2,3,4,5,6,7,8,9,10]
my_even_numbers = []
my_odd_numbers = []

for num in my_numbers :
    # print(num*10)
    if num %2 == 0:
        my_even_numbers.append(num)
        # print(f"this {num} is even")

    else :
        my_odd_numbers.append(num)
        # print(f"this {num} is odd")

print(f"the even list is {my_even_numbers}")
print(f"the even list is {my_odd_numbers}")
