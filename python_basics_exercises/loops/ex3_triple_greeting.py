##### Problem statement

# Write a loop that prints the value of the greeting variable three times.

##### Solution

greeting = 'Aloha!'

# 1. while loop solution

# counter = 0

# while counter < 3:
#     print(greeting)
#     counter += 1

# 2. for loop solution: most pythonic solution
# `_` is python convention for loop variable that isn't  used

for _ in range(3):    
    print(greeting)