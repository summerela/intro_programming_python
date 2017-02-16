from data import movies, boxart



#
#  Q2: write a function called `filterer`
#  that takes a the full List of `movies` and
#  returns a List of videos if a video has a rating equal to 5.0
#

# TODO: write `filterer` function here

# TODO: assign the variable `matches` to the output List from `filterer` function to make the test pass
# matches = your_filterer_function()

matches = []
print("[ MATCHES ]: {}".format(matches))
assert matches == [

    {'rating': 5.0, 'title': 'Bad Boys', 'bookmark':[{'id': 432534, 'time': 65876586}]
        ,'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 654356453},

    {'rating': 5.0, 'title': 'Fracture', 'bookmark': [{'id': 432534, 'time': 65876587}]
        ,'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 675465}
]
