##### Problem statement

# Using the datetime module in Python, how would you obtain 
# the current date and time?

##### Solution

# from python standard library reference, datetime section
# see examples of datetime usage

from datetime import datetime

current_datetime = datetime.now()

# use strftime() method to format a datetime object as a string

print(current_datetime.strftime('%a %b %d, %Y @ %I:%M %p'))