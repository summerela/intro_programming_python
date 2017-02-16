from data import movies, boxart

#
#  Q7:
#  write a function
#  that combines 'movies' and 'boxart' Lists
#  into a new List of tuples where
#  tuple index 0 is the movie and tuple index 1 is the boxart for that movie
#  NOTE: `movies` and `boxart` in sorted so that each movie index matches
#  the boxart index
#

# TODO: interleaved = your_function() to make the test pass
interleaved = []
print("[ INTERLEAVED ]: {}".format(interleaved))
assert interleaved == [
    (
        {'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 70111470, 'bookmark': [], 'rating': 4.0, 'title': 'Die Hard'},
        {'height': 200, 'width': 200, 'url': 'http://cdn-0.nflximg.com/images/2891/DieHard.jpg'}
    ),
    (
        {'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 654356453, 'bookmark': [{'id': 432534, 'time': 65876586}], 'rating': 5.0, 'title': 'Bad Boys'},
        {'height': 200, 'width': 150, 'url': 'http://cdn-0.nflximg.com/images/2891/BadBoys.jpg'}
    ),
    (
        {'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 65432445, 'bookmark': [], 'rating': 4.0, 'title': 'The Chamber'},
        {'height': 200, 'width': 300, 'url': 'http://cdn-0.nflximg.com/images/2891/TheChamber.jpg'}
    ),
    (
        {'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 675465, 'bookmark': [{'id': 432534, 'time': 65876587}], 'rating': 5.0, 'title': 'Fracture'},
        {'height': 150, 'width': 425, 'url': 'http://cdn-0.nflximg.com/images/2891/Fracture.jpg'}
    )
]
