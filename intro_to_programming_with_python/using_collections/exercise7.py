# 7. Write Python code to replace all the : characters in the 
# string below with +.

# Original solution based on methods in chapter

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info)   # print statement of original string for comparison to revised string
info_revised = info.split(':') # split creates list
print(info_revised)
print('+'.join(info_revised))

# Solution based on review of python documentation

# info_revised = info.replace(':', '+')  # replace ':' with '+'
# print(info_revised)