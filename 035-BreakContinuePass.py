# Break Continue Pass

my_numbers = [1,2,3,4,5,6,7,8,9,10,12,13,14,15]

# Continue
for num in my_numbers :
    if num == 13:
        continue
    print(num)

print("#"*20)

# break
for num in my_numbers :
    if num == 13:
        break
    print(num)

print("#"*20)

# Pass
for num in my_numbers :
   if num == 13 :
       pass 
    
