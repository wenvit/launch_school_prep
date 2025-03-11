# 6. Write a function that takes a string as an argument and 
# returns an all-caps version of the string when the string is 
# longer than 10 characters. Otherwise, it should return the 
# original string. 
# Example: change 'hello world' to 'HELLO WORLD', but 
# don't change 'goodbye'.
# 


def big_string_cap(my_string):
    if len(my_string) > 10:
        return my_string.upper()
    else:
        return my_string


print(big_string_cap('hello world'))
print(big_string_cap('goodbye'))

print(big_string_cap("Sue Smith"))     # Sue Smith
print(big_string_cap("Sue Roberts"))   # SUE ROBERTS
print(big_string_cap("Joe Shea"))      # Joe Shea
print(big_string_cap("Joe Stevens"))   # JOE STEVENS

print(big_string_cap(repr('')))
print(big_string_cap('abcdefghij'))
print(big_string_cap('abcdefghijk'))

print(big_string_cap('abcdefg1234'))