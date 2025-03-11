##### Problem statement

# Using the code below as a starting point, write a while loop 
# that prints the elements of lst at each index and terminates 
# after printing the last element of the list.

# lst = [1, 3, 7, 15]
# index = 0

# Further exploration: 
# What would the code output if lst is empty? Why is that?

##### Solution

#lst = [1, 3, 7, 15]
lst = []  # test
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

# If lst is empty, len(lst) is 0, so the 
# while expression `index < len(lst)` is falsy
# and never executes