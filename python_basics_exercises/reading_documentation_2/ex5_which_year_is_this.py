##### Problem

# The Python documentation for the datetime module 
# provides two attributes to retrieve the year from 
# a date or datetime object: year and isocalendar.

# from datetime import date

# today = date.today()

# today_year = today.year
# iso_year = today.isocalendar()[0]

# What is the difference between the year attribute 
# and the isocalendar method?

##### Solution

# Per datetime section of python standard library doc:

# today.year pulls the year attribute of the today date object
# The isocalendar method returns a tuple object with three components: 
# year, week, weekday.
# The code below pulls the year from the tuple returned by 
# the isocalendar method using the index 0
# The ISO calendar is a widely used variant of the Gregorian calendar. 
# The ISO year consists of 52 or 53 full weeks, and where a week starts on a
#  Monday and ends on a Sunday. The first week of an ISO year is the first 
# (Gregorian) calendar week of a year containing a Thursday. 
# This is called week number 1, and the ISO year of that Thursday is
#  the same as its Gregorian year.

from datetime import date

today = date.today()  # today method returns current local date

print(type(today)) # check type of object

today_year = today.year 
iso_year = today.isocalendar()[0] 

print(today_year)
print(today.isocalendar()) # print out what's returned by isocalendar
print(iso_year)
