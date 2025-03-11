# 9. Given the above code, answer the following questions and 
# explain your answers:

# my_list = [1, 2, 3, [4, 5, 6]]
# other_list = list(my_list)

# print(my_list)
# print(other_list)

# 1. Are the lists assigned to my_list and another_list equal?
# yes, these lists are equal because they contain the same values

# print(my_list == other_list)

# 2. Are the lists assigned to my_list and another_list the same object?
# i.e, are my_list and other_list pointing to the same object in memory
# no, these are not the same object
# list() constructor function creates a new list, a separate instance

# print(my_list is other_list)

# 3. Are the nested lists at index 3 of my_list and another_list equal?
# yes, the nested lists at index 3 are equal because
# they are equal values, same elements

# print(my_list[3])
# print(other_list[3])
# print(my_list[3] == other_list[3])

# 4. Are the nested lists at index 3 of my_list and another_list the same object?

# yes, they are the same object because the list() constructor
# creates a shallow copy....
# shallow copies do not include any new nested collections, 
# only a reference to the nested list gets copied
# consequence is that if nested list is mutated in my_list, it will modify
# the nested list in the copied list as well
# if want nested structures to be copies as well, must make deep copy
# constructor functions make shallow copies only


my_list = [1, 2, 3, [4, 5, 6], ['a', 'b']]
other_list = list(my_list)

#print(my_list[3] is other_list[3])

print(my_list)
print(other_list)

print(my_list[4] is other_list[4])

my_list[0] = 'test'
my_list[4][0] = 'new'

print(my_list)
print(other_list)