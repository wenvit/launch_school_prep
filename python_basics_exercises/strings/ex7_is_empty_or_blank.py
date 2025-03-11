##### Problem statement

# Write an is_empty_or_blank function to determine whether 
# a string is either empty or consists entirely of spaces. 
# For example:

# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True

##### Solution

# Again, rely on empty strings being falsy so return not string
# Also isspace() method returns True if string is entirely whitespace
# The return expression relies on `or` operator - one of the operands
# must be true to return True, otherwise it returns False

# def is_empty_or_blank(string):
#     return not string or string.isspace() 

# print(is_empty_or_blank('mars'))    # False
# print(is_empty_or_blank('  '))      # True
# print(is_empty_or_blank(''))        # True
# print(is_empty_or_blank('     \n')) # True
# print(is_empty_or_blank('   x'))    # False

# Solutions presented by Launch School
# str.strip method strips all beginning & trailing whitespace
# if the string consists of only whitespace,
# stripping whitespace results in empty string

# def is_empty_or_blank(string):
#     return string.strip() == ''

# print(is_empty_or_blank('mars'))    # False
# print(is_empty_or_blank('  '))      # True
# print(is_empty_or_blank(''))        # True

# def is_empty_or_blank(string):
#     return len(string.strip()) == 0

# print(is_empty_or_blank('mars'))    # False
# print(is_empty_or_blank('  '))      # True
# print(is_empty_or_blank(''))        # True

def is_empty_or_blank(string):
    return not string.strip()

print(is_empty_or_blank('mars'))    # False
print(is_empty_or_blank('  '))      # True
print(is_empty_or_blank(''))        # True

# More discussion from Launch School solution:
# `not` operator negates need to use bool constructor function
# because `not` always returns boolean value