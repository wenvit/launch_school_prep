# 8. Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

#print(text[21:35])                 # 'for the fjords'
#print(text[21:35].rfind('f'))     # 8

# this option slices first, which resets the string & indices for searhing
# then searching from the right on the slice for the first 'f'
# returns index 8


#print(text.rfind('f', 21, 35))    # 29

# this option retains the indices of the original string
# searching from the right between original indices of 21:35
# for the first 'f' returns 29