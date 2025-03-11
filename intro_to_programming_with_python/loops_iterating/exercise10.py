#10. The following code uses the randrange function from Python's random 
# library to obtain and print a random integer within a given range. 
# Using a while loop, it keeps running until it finds a random number 
# that matches the last number in the range. 
# Refactor the code so it doesn't require two different 
# invocations of randrange.

##### while loop
# while some condition is true
#    do some work

##### do/while loop
# do some work - will be executed at least once before checking for breaking condition
# while some condition is true

# typical pattern for python do/while loops is to set condition to while True:
# so this will be infinite unless there is a breaking condition

import random

highest = 10   # set an upper end for random number generator
# number = random.randrange(highest + 1)   # initialize number by invoking randrange
# print(number)  # print out the returned random int

# while number != highest:  # interate loop as long as the number not equal to upper end of range
#     number = random.randrange(highest + 1) # call randrange to select another number
#     print(number)

while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break