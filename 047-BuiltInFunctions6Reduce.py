# Built In Functions Part 6 Reduce

# reduce(function,Iterabel)

from functools import reduce

def sum_all(num1,num2):
    return num1+num2

numbers = [10,20,30,40]

sum_num = reduce(sum_all,numbers)

print(sum_num)
