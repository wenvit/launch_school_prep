# 2. Write a function, even_or_odd, that determines whether 
# its argument is an even or odd number. 
# If it's even, the function should print 'even'; 
# otherwise, it should print 'odd'. 
# Assume the argument is always an integer.

# Solution relies on truthiness
# If value % 2 is truthy (>0), value is odd
# If value % 2 is falsy (0), value is even
# def even_or_odd(value):
#     if value % 2:  
#         print('odd')
#     else:
#         print('even')

# even_or_odd(-2)


#############
# Another way

# def even_or_odd(value):
#     print('odd' if value % 2 else 'even')

# even_or_odd(3)

##############
# Launch School solution - maybe this is more clear?

def even_or_odd(value):
    if value % 2 == 0:
        print('even')
    else:
        print('odd')

even_or_odd(-3)