# -*- coding: utf-8 -*-
#!/usr/bin/env python3

header = ['FirstName', 'LastName', 'City', 'Zipcode']
row1 = ['Greg', 'Corradini', 'Minneapolis', '75432']
row2 = ['Summer', 'Rae', 'Seattle', '98103']
# this nested list `table` represents
# a table of rows where the first row
# is the column headers
table = [
    header,
    row1,
    row2,
]

# calculate the max width of the table cell
padding = 2
max_width = 0
for row in table:
    new_max = max([len(value) for value in row]) + padding
    # only set thew new max if it's actually greater
    if new_max > max_width:
        max_width = new_max

# # print out each row of the table
# for row in table:
#     cell1, cell2, cell3, cell4 = row
#
#     # TODO: use the print() function and string formatting to create output that looks sorta/kinda/similar ( but not identical ) to
#     #
#     # |FirstName    |LastName     |City         |Zipcode      |
#     # |Greg         |Corradini    |Minneapolis  |75432        |
#     # |Summer       |Rae          |Seattle      |98103        |
#     #
#     # WRITE YOUR CODE BELOW:
#     print(cell1,cell2,cell3,cell4)


print("\nMETHOD 1: using tabs\n")
# print out each row of the table
for row in table:
    cell1, cell2, cell3, cell4 = row

    # TODO: use the print() function and string formatting to create output that looks sorta/kinda/similar ( but not identical ) to
    #
    # |FirstName    |LastName     |City         |Zipcode      |
    # |Greg         |Corradini    |Minneapolis  |75432        |
    # |Summer       |Rae          |Seattle      |98103        |
    #
    # WRITE YOUR CODE BELOW:
    print("|{}\t|{}\t|{}\t|{}\t|".format(cell1,cell2,cell3,cell4))


print("\nMETHOD 2: using spaces\n")
# print out each row of the table
for row in table:
    cell1, cell2, cell3, cell4 = row

    # TODO: use the print() function and string formatting to create output that looks sorta/kinda/similar ( but not identical ) to
    # |FirstName    |LastName     |City         |Zipcode      |
    # |Greg         |Corradini    |Minneapolis  |75432        |
    # |Summer       |Rae          |Seattle      |98103        |
    # WRITE YOUR CODE BELOW:
    print("|{}    |{}    |{}    |{}    |".format(cell1,cell2,cell3,cell4))


print("\nMETHOD 3: using string functions you haven't learned about yet\n")
# print out each row of the table
for row in table:
    cell1, cell2, cell3, cell4 = row

    # TODO: use the print() function and string formatting to create output that looks sorta/kinda/similar ( but not identical ) to
    #
    # |FirstName    |LastName     |City         |Zipcode      |
    # |Greg         |Corradini    |Minneapolis  |75432        |
    # |Summer       |Rae          |Seattle      |98103        |
    #
    # WRITE YOUR CODE BELOW:
    print("|{}|{}|{}|{}|".format(cell1.ljust(max_width),cell2.ljust(max_width),cell3.ljust(max_width),cell4.ljust(max_width)))

print("\nMETHOD 4: advanced shennanigans you might be interested in learning more about\n")
# print out each row of the table
header = table[0]
for row in table:
    # zip takes two lists and interleaves them. Example:
    # list1 = ['a','b','c']
    # list2 = [1,2,3]
    # zipped = zip(list1,list2)
    # print( zipped )
    # [('a',1),('b',2),('c',3)]
    record = dict(zip(header,row))
    record.update({'width': max_width})

    # TODO: use the print() function and string formatting to create output that looks sorta/kinda/similar ( but not identical ) to
    #
    # |FirstName    |LastName     |City         |Zipcode      |
    # |Greg         |Corradini    |Minneapolis  |75432        |
    # |Summer       |Rae          |Seattle      |98103        |
    # WRITE YOUR CODE BELOW:
    print("|{FirstName:<{width}}|{LastName:<{width}}|{City:<{width}}|{Zipcode:<{width}}|".format( **record ))