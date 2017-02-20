from data import movies, boxart


#
#  Q1:
#  write a function called `transformer`
#  that takes the List 'movies'
#  and returns an List of {id,title} pairs
#

# TODO: write `transformer` function here

# TODO: assign the variable `pairs` to the output List from `transformer` function to make the test pass
# pairs = your_transformer_function()
pairs = []
print("[ PAIRS ]: {}".format(pairs))
assert pairs == [
    {'id': 70111470, 'title': 'Die Hard'},
    {'id': 654356453, 'title': 'Bad Boys'},
    {'id': 65432445, 'title': 'The Chamber'},
    {'id': 675465, 'title': 'Fracture'}
]
