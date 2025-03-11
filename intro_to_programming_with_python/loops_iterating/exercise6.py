# 6. Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. 
# In this problem, you should write code that creates a new list 
# with one element for each number in my_list. 
# If the original number is an even, then the corresponding element 
# in the new list should contain the string 'even'; 
# otherwise, the element should contain 'odd'.

from pprint import pp

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# result_list = []

# for number in my_list:
#     if number % 2 == 0:
#         result = 'even'
#     else:
#         result = 'odd'
#     result_list.append(result)

# pp(result_list)

########## I like this Launch School solution
# list comprehension works well for list transformations
# this solution relies on helper function to make list comprehension
# easier to read

# def even_or_odd(number):
#     return 'even' if number % 2 == 0 else 'odd'

# result_list = [ even_or_odd(number) for number in my_list ]
# pp(result_list)

#### Another solution using a ternary expression, which is not as easy to read

result_list = [ 'even' if number % 2 == 0 else 'odd'
               for number in my_list ]

pp(result_list)

