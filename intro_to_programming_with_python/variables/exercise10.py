# 10. Assume that obj already has a value of 42 when the code below starts 
# running. Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references?
# Which statements do neither? If necessary, you can read the documentation.

obj = 42           # initialize obj variable to immutable integer

obj = 'ABcd'       # reassignment of obj to immutable string

print(f"Value of obj after obj = 'ABcd': {obj}")

obj.upper()        # neither, upper() method invoked on string 
                   # returns copy of string with
                   # all uppercase letters but doesn't modify original string
                   # (strings are immutable)
                   # and results of applying this method aren't captured
                   # in variable obj

print(f"Value of obj after obj.upper(): {obj}")

obj = obj.lower()  # reassignment, in this case, the results of invoking 
                   #  the lower() method are captured in the obj variable
print(f"Value of obj after obj = obj.lower(): {obj}")

print(len(obj))    # neither, this simply prints out length of obj as int
print(f"Value of obj after print(len(obj)): {obj}")

obj = list(obj)    # reassignment, invoke list() constructor function
                   # and capture in variable obj
print(f"Value of obj after obj = list(obj): {obj}")

obj.pop()          # mutation of list object, pop() method removes last
                   # element of list
print(f"Value of obj after obj.pop(): {obj}")

obj[2] = 'X'       # mutation of list object based on index assignment
                   # index assignment: assign a value to element at index[x]
print(f"Value of obj after obj[2] = 'X': {obj}")

obj.sort()         # mutation, invoking sort method 
                   # sorts list elements in place
                   # note that uppercase letters are less than any 
                   # lowercase letters
print(f"Value of obj after obj.sort()': {obj}")

set(obj)           # neither, results of applying set() constructor function
                   # are not captured in obj variable
print(f"Value of obj after set(obj)': {obj}")

obj = tuple(obj)   # reassignment, results of applying tuple() constructor 
                   # function are captured in variable obj
print(f"Value of obj after obj = tuple(obj)': {obj}")