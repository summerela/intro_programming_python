# -*- coding: utf-8 -*-
#!/usr/bin/env python3

header = ['FirstName', 'LastName', 'City', 'Zipcode']
row1 = ['Greg', 'Corradini', 'Minneapolis', '75432']
row2 = ['Summer', 'Rae', 'Seattle', '98103']
# this nested list `table` represents
a table of rows where the first row
# is the column headers
table = [
    header,
    row1,
    row2,
]

calculate the max width of the table cell
padding = 2
max_width = 0
for row in table:
    new_max = max([len(value) for value in row]) + padding
    # only set thew new max if it's actually greater
    if new_max > max_width:
        max_width = new_max


print out each row of the table
for row in table:
    cell1, cell2, cell3, cell4 = row

    # TODO: use the print() function and string formatting to create output that looks sorta/kinda/similar ( but not identical ) to a table
    #
    # |FirstName    |LastName    |City    |Zipcode    |
    # |Greg    |Corradini    |Minneapolis    |75432    |
    # |Summer    |Rae    |Seattle    |98103    |
    #
    # WRITE YOUR CODE BELOW:
    print(cell1,cell2,cell3,cell4, sep='|')