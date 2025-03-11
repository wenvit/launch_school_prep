# Identify the data type or class for each of the following values:

#'True'          string, str
#False           boolean, bool
#(1, 2, 3)       tuple
#1.5             float
#[1, 2, 3]       list
#2               integer, int
#range(5)        range
#{1, 2, 3}       set
#None            NoneType
#{'foo': 'bar'}  dictionary, dict


# Check

list_of_objects = [
    'True',
    False,
    (1, 2, 3),
    1.5,
    [1, 2, 3],
    2,
    range(5),
    {1, 2, 3},
    None,
    {'foo': 'bar'},
]

for obj in list_of_objects:
    print(obj, 'is a', type(obj).__name__)
