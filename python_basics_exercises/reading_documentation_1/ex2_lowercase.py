###### Problem statement

# Determine whether Python has a method to lowercase a string, 
# for example converting 'Aloha, World!' into 'aloha, world!.

###### Solution

# In the python standard library documentation, from the table of contents, click on 
# "Text Sequence Type - str" for a list of string methods.

# str.lower()

# str.casefold() is another option and has the additional benefit of being able to 
# handle non-English characters

# Example

text = 'Aloha, World!'

print(text.lower())
print(text.casefold())







