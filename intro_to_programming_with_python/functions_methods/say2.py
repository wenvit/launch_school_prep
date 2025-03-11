# def say(text):
#     print(text)


# say('Hello')
# say('Hi')
# say('How do you do?')
# say('Quite all right')

#################################
## default parameters


def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!
say()        # hello!