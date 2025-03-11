##### Problem statement

# In the following code snippet, find all violations of the PEP8 style guide. 
# Rewrite it so that it conforms with the guide.

# iceCreamDensity=10

# while iceCreamDensity>0 :
#    print('Drip...')
#    iceCreamDensity-=1

# print('The ice cream melted.')

##### Solution

# Line 6, initialization of iceCreamDensity variable:
#         1. variable names should be lowercase with underscores 
#            to separate words to improve readability 
#         2. spaces should be used on both sides of assignment operator (=)
# Line 8, while condition: 
#         1. spaces should be used on both sides of greater than operator (>)
#         2. extraneous space before colon should be removed
# Line 10: spaces should be used on both sides of augmented assignment operator (-=)

# Rewrite following PEP8 guidelines:
# 1. change iceCreamDensity to ice_cream_density 
# 2. add spaces on both sides of `=`, `>`, and `-=` operators 
# 3. remove space before `:` in while loop 

ice_cream_density = 10  

while ice_cream_density > 0: 
    print('Drip...')
    ice_cream_density -= 1   

print('The ice cream melted.')
