##### Problem statement

# Modify the following code so the loop continues iterating 
# until the user inputs 'yes'.

# while True:
#     print('Should I stop looping?')
#     answer = input()

##### Solution

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    print('Incorrect answer. Please enter "yes."')  # Launch School suggestion