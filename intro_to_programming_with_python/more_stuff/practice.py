### Function composition

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def times(num1, num2):
#     return num1 * num2

# sum = add(20, 45)
# print(sum)

# difference = subtract(80, 10)
# print(difference)

# Here's how to do it using composition

# print(add(20, 45))
# print(subtract(80, 10))

# more interesting example

#print(times(add(20, 45), subtract(80, 10)))

#### Method Chaining

# letters = 'abcdefghijklmnoqrstuvwxyz'

# Note that the parentheses surrounding this
# multi-line chain are required.
# consonants = (letters.replace('a', '').
#                       replace('e', '').
#                       replace('i', '').
#                       replace('o', '').
#                       replace('u', ''))
# print(consonants)    # bcdfghjklmnqrstvwxyz


##### Modules

# from datetime import datetime as dt

# date = dt.strptime('July 16, 2022', '%B %d, %Y')
# print(date)
# weekday_name = date.strftime('%A')
# print(weekday_name)

###### Function Defition Order

# This code works! Python doesn't really care about the 
# order of defining functions as long as all functions are
# defined before invoking

# def top():
#     bottom()

# def bottom():
#     print('Reached the bottom')

# top()

#### Nested Functions

# def foo():
#     def bar():
#         print('BAR')

#     bar()

# foo()
# bar()

##### Global and nonlocal statements

## Example with global greeting variable 
# used within function

# greeting = 'Salutations'

# def well_howdy(who):
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

## Example with local greeting variable defined
# locally within function that overrides global greeting

# greeting = 'Salutations'  # global variable greeting

# def well_howdy(who):
#     greeting = 'Howdy'   # local variable greeting - variable shadowing
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

## Example using global greeting statement 

greeting = 'Salutations'

def well_howdy(who):
# the global greeting line tells python that the reassignment of greeting to
# 'Howdy' within the function will update the global value of greeting
    global greeting  
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)

# def set_pi():
#     global pi
#     pi = 3.1415

# set_pi()
# print(pi)