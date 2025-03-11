##### Problem statement

# Use the Python documentation for the str class to determine
# which method can be used to right justify a str object.

##### Solution

# From documentation, str.rjust() method achieves this.  
# str.rjust(width[, fillchar])
# Return the string right justified in a string of length width. 
# Padding is done using the specified fillchar (default is an ASCII space). 
# The original string is returned if width is less than or equal to len(s).

text = 'right justify test'

print(text.rjust(25))
print(text.rjust(25, '*'))