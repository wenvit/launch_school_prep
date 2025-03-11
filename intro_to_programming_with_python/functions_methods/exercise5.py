# 5. What does the following code print?

# def scream(words):
#     return words + '!!!!'

# scream('Yipeee')

###############
# This code doesn't print anything.

# The definition of the scream function begins on line 3.
# scream has a single parameter called words. It returns a value 
# consisting of a string concatenation of words and 4 exclamation points. 
# When the scream function is invoked on line 6, it passes an argument of 'Yipeee'
# to the parameter words. 
# However, there is no print statement to print the results of invoking scream


##########################
# Several ways to fix it

# def scream(words):
#     return words + '!!!!'

# print(scream('Yipeee'))

#######################
# def scream(words):
#     return words + '!!!!'

# screamed_message = scream('Yipeee')
# print(screamed_message)

######################

def scream(words):
    print(words + '!!!!')

scream('Yipeee')
