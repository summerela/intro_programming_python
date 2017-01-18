# -*- coding: utf-8 -*-
#!/usr/bin/env python3

this nested list represents
a table of rows where the first row
is the column headers
table = [
    ['FirstName', 'LastName', 'City', 'Zipcode'],
    ['Greg', 'Corradini', 'Minneapolis', '75432'],
    ['Summer', 'Rae', 'Seattle', '98103'],
]

calculate the max width
padding = 2
max_width = 0
for row in table:
    new_max = max([len(value) for value in row]) + padding
    only set thew new max if it's actually greater
    if new_max > max_width:
        max_width = new_max

render the table to stdout console with print
header = table[0]
only loop through the rows, skip the header
for row in table[1:]:
    # zip takes two lists and interleaves them. Example:
    # list1 = ['a','b','c']
    # list2 = [1,2,3]
    # zipped = zip(list1,list2)
    # print( zipped )
    # [('a',1),('b',2),('c',3)]
    record = dict(zip(header,row))
    record.update({'width': max_width})
    print("|{FirstName:<{width}}|{LastName:<{width}}|{City:<{width}}|{Zipcode:<{width}}|".format( **record ))