##### Problem statement

# The following code raises a SyntaxError:

# speed_limit = 60
# current_speed = 80

# if current_speed > speed_limit
#     print('"People are so bad at driving cars that '
#           "computers don\'t have to be that good to be "
#           'much better." -- Marc Andreessen')
    
# What does a SyntaxError indicate? Try running the above code, 
# then use the resulting error message to fix the error.

##### Solution

# The python standard library reference, built-in exceptions documentation
# states: Raised when the parser encounters a syntax error. 

# When the original code above is run, the SyntaxError message states
# that a ':' was expected. Here's the fix:

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')