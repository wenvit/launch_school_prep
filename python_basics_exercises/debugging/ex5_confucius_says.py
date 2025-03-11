##### Problem statement

# You want to have a small script delivering motivational quotes, 
# but with the following code you run into a very common error message: 
# TypeError: can only concatenate str (not "NoneType") to str. 
# What is the problem and how can you fix it?

# def get_quote(person):
#     if person == 'Yoda':
#         'Do. Or do not. There is no try.'
#     if person == 'Confucius':
#         'I hear and I forget. I see and I remember. I do and I understand.'
#     if person == 'Einstein':
#         'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

# print('Confucius says:')
# print('"' + get_quote('Confucius') + '"')

##### Solution

# This code will raise the TypeError message because the function `get_quote` 
# doesn't explicitly return a value, so a default value of `None` is returned. 
# On line 17, the print function is invoked with a string argument
# consisting of quotation marks enclosed in single quotes (strings) 
# concatenated with the return value of the
# get_quote function. python raises an error when attempting to 
# concatenate strings with `None`

# Here's a fix:

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')