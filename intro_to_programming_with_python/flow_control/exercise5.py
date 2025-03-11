#5. What does this code output, and why?


def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])
is_list_empty([False])  # truthy, even though element in list is falsy

# Running this code prints Empty
# is_list_empty function is called by passing an empty list ([])
# as an argument to parameter my_list
# The if/else expression in the body of the function first
# checks if my_list is truthy. An empty list is falsy so it
# passes on to the else block and prints Empty

