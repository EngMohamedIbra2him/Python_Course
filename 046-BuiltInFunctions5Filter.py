#  Built In Functions Part 5 Filter

# filter(function,iterable)
def check_number(num):
    if num > 10:
        return num
    
list_numbers = [1,2,3,4,5,6,7,8,9,10,11]

filter_number = filter(check_number,list_numbers)

for i in filter_number :
    print(i)