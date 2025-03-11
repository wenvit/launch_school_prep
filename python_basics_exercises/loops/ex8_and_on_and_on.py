##### Problem statement

# The following code keeps looping forever. (You can hit Ctrl-C to stop it.)
# Why does the loop keep running? 
# Modify it so that it stops after the first iteration.

# while True:
#     print("and on")

##### Solution

# The above while loop is an infinite loop because the while condition never
# stops being True. True always evaluates to True.


# Here's a fix - break exits out of current loop

while True:
    print('and on')
    break