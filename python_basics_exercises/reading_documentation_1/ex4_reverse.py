##### Problem statement

# Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

##### Solution

# Python doesn't have a built in method for reversing a string. 
# Here's a way to accomplish this using slicing:

text = 'hello'

print(text[::-1])