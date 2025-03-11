# def well_howdy(who):
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')


# well_howdy('Angie')

# generates error because greeting variable only 
# defined within well_howdy function
# print(greeting)  

####################################

# Example showing greeting defined outside function
# and a separate definition of greeting inside function
# assignment of greeting within function hides the greeting
# variable outside function 


# greeting = 'Salutations'

# def well_howdy(who):
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

#######################
# In this example, python looks for value of greeting 
# in the lexical scope

# greeting = 'Salutations'

# def well_howdy(who):
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

#######################

def scope_test():
    if True:
        foo = 'Hello'
    else:
        bar = 'Goodbye'

    print(foo)
    print(bar)

scope_test()