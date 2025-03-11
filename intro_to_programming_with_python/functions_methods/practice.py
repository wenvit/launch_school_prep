# misc code from Functions and Methods chapter

# def hello():
#     print('Hello')
#     return True

# hello()
# print(hello())

# check what print function returns

# print(print())

# def well_howdy(who):
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')
#     return greeting

# well_howdy('Michelle')
# test = well_howdy('Wendy')
# print(test)

# greeting = 'Salutations'

# def well_howdy(who):
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')

# well_howdy('Lily')
# print(greeting)

# greeting = 'Salutations'

# def well_howdy(who):
#     print(f'{greeting}, {who}')

# well_howdy('Blue')
# print(greeting)

###############################
# Discussion of mutating the caller

# note that the function doesn't return the 
# list, but it mutates the list
# difficult to debug

# def add_new_number(my_list):
#     my_list.append(9)

# numbers = [1, 2, 3, 4, 5]
# add_new_number(numbers)
# print(numbers)

# Better practice is to return a new object

def add_new_number(my_list):
    return my_list + [9]

numbers = [1, 2, 3, 4, 5]
new_numbers = add_new_number(numbers)

print(new_numbers)
print(numbers)