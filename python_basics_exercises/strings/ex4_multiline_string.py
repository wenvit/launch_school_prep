##### Problem statement

# How can you assign the following rhyme to a single variable 
# while preserving the line break?

# A pirate I was meant to be!
# Trim the sails and roam the sea!

##### Solution

# keep in mind with triple quotes, all white space is printed out so be aware
# of indents, spacing etc

rhyme = '''A pirate I was meant to be!
Trim the sails and roam the sea!'''

print(rhyme)

# Another way

rhyme = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'

print(rhyme)