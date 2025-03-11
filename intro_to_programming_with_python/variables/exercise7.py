# 7. What happens when you run the following code? Why?

# Code will print out the greetings to Victor, followed by greetings to Nina
# print() statements are appropriate string concatenation format
# However, reassigning NAME variable doesn't follow python conventions
# because all cap variable NAME denotes a constant variable and this code
# reassigns the value to Nina

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)