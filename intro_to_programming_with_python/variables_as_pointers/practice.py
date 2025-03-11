import copy

orig = [[1, 2], 3, 4]

###### Shallow copies

# dup = copy.copy(orig)

# print(orig is dup) # False because orig and dup not same object
# print(orig == dup) # True

# orig[2] = 44
# print(dup)         # [[1, 2], 3, 4] integers are copies

# print(orig[0] is dup[0]) # True, nested list is same object
# orig[0][1] == 22
# print(dup[0])      # [1, 22]

####### Deep copies

dup = copy.deepcopy(orig)

print(orig is dup)    # False
print(orig == dup)    # True

orig[2] = 44
print(dup)            # [[1, 2], 3, 4]

print(orig[0] is dup[0]) # False
orig[0][1] = 22
print(dup[0])         # [1, 2]