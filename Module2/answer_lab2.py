
def odd_or_even(i):
    if i%2 == 0:
       answer = 'even'
    else:
       answer = 'odd'
    return answer


def for_this(j):
    for i in range(j):
        answer = odd_or_even(i)
        print("{} is {}".format(i, answer))

for_this(10)
