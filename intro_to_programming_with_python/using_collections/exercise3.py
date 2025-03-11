# 3. Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

# this solution works for any length tuple
orig_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# reversed is iterator so need to use tuple constructor function
new_tuple = tuple(reversed(orig_tuple))   # (5, 4, 3, 2, 1)
print(new_tuple)
print(new_tuple[1:-1])                    # start index 1: stop index -1 (not inclusive)

###################
# Other solutions

# orig_tuple = (1, 2, 3, 4, 5)
# my_list = list(orig_tuple)
# my_list.reverse()   # method is mutating, so don't have to capture with new variable
# new_tuple = tuple(my_list)
# print(new_tuple[1:-1])

# orig_tuple = (1, 2, 3, 4, 5)
# new_tuple = orig_tuple[3:0:-1]
# print(new_tuple)

# solution that also works with any length tuple
# orig_tuple = (1, 2, 3, 4, 5)
# new_tuple = orig_tuple[-2:0:-1]
# print(new_tuple)

# orig_tuple = (1, 2, 3, 4, 5)
# new_tuple = orig_tuple[-2:-5:-1]
# print(new_tuple)


