# list comprehension example

# squares = [number * number for number in range(5)]
# print(squares)

# this is the same as following for loop:

# squares = []
# for number in range(5):
#     square = number * number
#     squares.append(square)

# print(squares)

# a selection example

# multiples_of_6 = [ number 
#                    for number in range(20)
#                    if number % 6 == 0 ]
# print(multiples_of_6)

# example combining selection and transformation

# even_squares = [ number * number
#                 for number in range(10)
#                 if number % 2 == 0 ]
# print(even_squares)

# example using dictionary

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

#names = [ name.upper() for name in cats_colors ]
# names = [ name.upper()
#          for name in cats_colors
#          if cats_colors[name] == 'orange' ]
# names = [ name.upper()
#          for name in cats_colors
#          if cats_colors[name] == 'orange'
#          if name[0] == 'L' ]

# print(names)

# example with muleiple for loops

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = [ f'{rank} of {suit}'
        for suit in suits
        for rank in ranks ]

print(deck)