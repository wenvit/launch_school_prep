##### Problem statement

# Write code that capitalizes the words in the string 
# 'launch school tech & talk', so that you get the string 
# 'Launch School Tech & Talk'.

##### Solution

string_original = 'launch school tech & talk'
# string_title = string_original.title()

# print(string_title)

# Another option based on Launch School solution

def capitalize(string):
    words = string.split()

    words_lst = []
    for word in words:
        words_lst.append(word.capitalize())

    words_cap = ' '.join(words_lst)

    return words_cap

string_uppercase = capitalize(string_original)

print(string_uppercase)



