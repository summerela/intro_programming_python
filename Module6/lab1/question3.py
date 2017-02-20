from data import movies, boxart


#
#  Q3: write a function
#  that filters the List of 'movies'
#  into a new List of videos if a video has a rating equal to 5.0
#  but only return movie {id,title} pairs
#

# TODO: pairs = your_function() and make the test pass
pairs = []
print("[ PAIRS ]: {}".format(pairs))
assert pairs == [
    {'id': 654356453, 'title': 'Bad Boys'},
    {'id': 675465, 'title': 'Fracture'}
]