##### Problem statement

# Our predict_weather function should output a message indicating whether 
# a sunny or cloudy day lies ahead. However, the output is the same every
#  time the function is invoked. Why? Fix the code so that it behaves as expected.

# import random

# def predict_weather():
#     sunshine = random.choice(['True', 'False'])

#     if sunshine:
#         print("Today's weather will be sunny!")
#     else:
#         print("Today's weather will be cloudy!")

##### Solution

import random

def predict_weather():
#    sunshine = random.choice(['True', 'False']) # original problematic line
    sunshine = random.choice([True, False])  # fixed code

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

# As originally written, this function prints
# "Today's weather will be sunny!"
# every time the function is invoked.
# This is because on line 22, the sunshine variable is set to either 
# 'True' or 'False' string values. These are strings, not boolean
# True or False values. The `is sunshine` statement on line 24
# always evaluates to truthy because the sunshine variable is always set to a string
# or truthy value. Strings are truthy; empty strings ('') are falsy. 
# To fix this code, on line 22 for the sunshine variable initialization,
# change 'True' and 'False' to the boolean True and Valse