##### Problem statement

# Take your code from the previous Check the Weather exercise and rewrite 
# it as a match-case statement. Feel free to add more cases besides 
# 'sunny' and 'rainy'.

##### Solution

# weather = 'sunny'
# weather = 'cloudy'
# weather = 'rainy'
weather = 'snowy'

match weather:
    case 'sunny':
        print("It's a beautiful day.")
    case 'rainy':
        print('Grab your umbrella.')
    case 'snowy':
        print('Wear your boots.')
    case _:
        print("Let's stay inside.")

