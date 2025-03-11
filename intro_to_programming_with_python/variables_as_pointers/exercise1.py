# 1. In your own words, explain the difference 
# between these two expressions.

# my_object1 == my_object2
# my_object1 is my_object2

# The expression on line 4 evaluates whether my_object1 and my_object2 
# have the same value (length, elements)
# Value equality doesn't always mean same type (e.g., int and float can be equivalent)

# The expression on line 5 evaluates whether my_object1 and my_object2
# are the same object (pointers referencing the same object in memory)
# Literals will not be the same object


a = [1, 2, 3]
b = a

print(a)
print(b)

a.append('xxxxxx')
print(b)