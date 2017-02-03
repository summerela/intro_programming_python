""" This script asks the users for two numbers, places them in a list,
then tells the user the index location of each number, and if it is
divisible by 3.

The user could break this script by not providing a minimum number
that is less than the maximum number.  I have used while to prompt 
the user to enter a new maximum, if it is less than or equal to minimum """

#!/bin/env python

var1 = int(input("Enter a minimum number: "))
var2 = int(input("Enter a maximum number: "))

# this checks that the user has entered a maximum that is greater than the minimum
while var1 >= var2:
    var2 = int(input("The maximum cannot be less than or equal to the minimum.  Please try again: "))


# this allows the maximum number to be included in the list
var3 = var2 + 1

my_list = list(range(var1, var3))

def list_numbers(num):
    for index, my_num in enumerate(num):
        print("The number {} is at index {}".format(my_num, index))

list_numbers(my_list)

def divide_numbers(num):
    for x in num:
        if x % 3 == 0:
            print("The number {} is divisible by 3".format(x))
        else: 
        	pass

divide_numbers(my_list)

quit()
