##### Problem statement

# You want to add the numbers from 1 to 5 to a list, 
# but the code below is not producing the expected result. How can you fix it?

# numbers = []

# for i in range(5):
#     numbers.append(i)

# print(numbers)

##### Solution

# This code outputs [0, 1, 2, 3, 4]
# This is because the range function invoked on line 8 starts wih 0
# by default, with a stop value of 5 which is non-inclusive. 
# To fix, the range function should be given a start of 1
# and a top of 6 (stop is always non-inclusive)

numbers = []

for i in range(1, 6 ):
    numbers.append(i)

print(numbers)