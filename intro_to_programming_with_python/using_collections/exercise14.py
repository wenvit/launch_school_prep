# 14. Assume you have the following sequences:

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)   # 10, 20, 30, 40, 50 

# Write some code that combines the sequences into a list of tuples. 
# Each tuple should contain one member of each sequence. 
# Print the final result so you can see all the values:

# zip function will create tuples from each sequence, as many as it can from the shortest sequence
# zip will compiles these in order given, order matters
# outputs an iterator object, which we convert to a list using list constructor function

zipped_iterables = zip(my_str, my_list, my_tuple, my_range)

print(list(zipped_iterables))