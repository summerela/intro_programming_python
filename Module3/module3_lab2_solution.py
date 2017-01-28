# -*- coding: utf-8 -*-
#!/usr/bin/env python3

def odd_or_even(i):
    if i%2 == 0:
       answer = 'even'
    else:
       answer = 'odd'
    return answer

# 1
print("\n[ SOLUTION 1 ]: simple for loop calling into `odd_or_even` function: \n")
for i in range(10):
    answer = odd_or_even(i)
    print("{} is {}".format(i, answer))

# 2
print("\n[ SOLUTION 2 ]: moving for loop into it's own function that calls another function: \n")
def second_function(j):
    for i in range(j):
        answer = odd_or_even(i)
        print("{} is {}".format(i, answer))

second_function(10) # make sure to call it to execute it!

# 3
print("\n[ SOLUTION 3 ]: moving for loop into the same function as `odd_or_even`. NOTE: \
that this actually changes the meaning of the `odd_or_even` function. In the last two solutions \
`odd_or_even` told us whether a single integer argument was odd or even. Now it's telling us whether a \
range of integers are odd or even. Also compare this solution that only prints out the answer \
with the next more advanced solution that also returns the answers: \n")
def odd_or_even_range(i):
    for i in range(i):
        if i%2 == 0:
           answer = 'even'
        else:
           answer = 'odd'
        print("{} is {}".format(i, answer))

odd_or_even_range(10) # make sure to call it to execute it!

# 4
print("\n[ SOLUTION 4 ]: this was the extra question on lab2. Here we do the same thing as solution 3 \
but return the answer(s) also: \n")
def odd_or_even_range(i):
    answers = []
    for i in range(i):
        if i%2 == 0:
           answer = 'even'
        else:
           answer = 'odd'
        print("{} is {}".format(i, answer))
        answers.append(answer)
    return answers

print(odd_or_even_range(10)) # make sure to call it to execute it!
