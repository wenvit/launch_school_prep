# 2. Take a look at this code snippet. What does this program
# print and why?

# foo = 'bar'

# def set_foo():
#     foo = 'qux' # variable shadowing

# set_foo() 
# print(set_foo())  added this to check return value 
# print(foo)
########################

# This code prints the string value 'bar'

# The variable foo is initialized to a string value of 'bar'
# in the global scope of this code (line 4). 
# The definition of the set_foo function begins on line 6.
# The function has no parameters. The function simply initializes a local variable foo 
# by assigning it to the string value of 'qux' and returns a default
# value of None. Because this foo variable is local to set_foo function,
# it is a separate variable from the global foo variable.
# This is an example of variable shadowing...a variable with a local
# scope has the same name as a variable in the global scope.
# When set_foo is invoked on line 9, the local variable foo is set to 'qux'
# but None is returned.
# When the print function is invoked with the foo argument (line 11), it
# prints the value of foo it finds in the global scope


########################
# A variation

# foo = 'bar'

# def set_foo():
#     foo = 'qux'
#     return foo

# foo = set_foo() 

# print(foo)  # now prints 'qux' because foo has been reassigned in global scope

########################
# Another variation

# foo = 'bar'

# def set_foo():
#     foo = 'qux'
#     print(foo) # prints 'qux' because python searches local scope first

# set_foo() 
# print(foo)  # prints 'bar' 

########################
# Another variation

# foo = 'bar'

# def set_foo():
#     print(foo)  # within local scope, print function will search outer scopes

# set_foo() 
# print(foo)  