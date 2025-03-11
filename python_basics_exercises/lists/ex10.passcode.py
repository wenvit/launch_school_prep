##### Problem statement

# We generated parts of a passcode and now want to combine 
# them into a string. Write some code that creates and prints 
# a string that contains each portion of the passcode separated 
# by hyphens (-).

##### Solution

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

# Write some code here.

# Most straightforward approach using join method

# passcode_complete = '-'.join(passcode)
# print(passcode_complete)

# Try this long-hand solution from Launch School
# works but join method is a lot cleaner and simpler

passcode_complete = ''

for i in range(len(passcode)):
    if i > 0:
        passcode_complete += '-'

    passcode_complete += passcode[i]

print(passcode_complete)