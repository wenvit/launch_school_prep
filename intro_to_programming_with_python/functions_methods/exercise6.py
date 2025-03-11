# 6. What does the following code print?

# def scream(words):
#     words = words + '!!!!'
#     return
#     print(words)

# scream('Yipeee')

###############

# This doesn't print anything because the return terminates the function
# before the print statement is executed. It returns a value of None.

# The definition of the scream function begins on line 3. It has a single
# parameter called words. Within the body of the function, the local variable words
# is reassigned to a value resulting from 
# string concatenation of words and four exclamation points.
# It then returns before the print call.
# scream is invoked on line 8 with an argument 'Yippeee'

###################
# To fix ....does it need the return key word?
def scream(words):
    words = words + '!!!!'
    print(words)
    return

scream('Yipeee')

 
