#!/bin/env python

#Input two numbers
num1 = int(input("Give me your first number: "))
num2 = int(input("Give me your second number: "))

#function to find max number in the inputed set
def findmax(num1,num2):
	if num1 > num2:
		maximum = num1
	else:
   		maximum = num2
	return(maximum)

#function to find min number in the inputed set
def findmin(num1,num2):
	if num1 < num2:
		minimum = num1
	else:
   		minimum = num2
	return(minimum)

#variable to create range between max and min in the inputed set
#variable finds the difference between max and min number in the inputed set
maxminrange = findmax(num1,num2)-findmin(num1,num2)

#for loop that builds list of numbers between max and min number
#enumerate is used to locate the number and position in the list
#1 is added to the counter in order to adjust for the non-inclusive counting method
#if statement and modulo is used to determine divisibility by 3
mylist = []
for number,index in enumerate(range(maxminrange+1)):
	mylist.append(number+findmin(num1,num2))
	if (number+findmin(num1,num2)) % 3 == 0:
		answer = "This number {} is divisible by 3.".format(number+findmin(num1,num2))
	else:
		answer = "This number {} is NOT divisible by 3.".format(number+findmin(num1,num2))
	print("This number {} is at index {}.".format(number+findmin(num1,num2), index),"\t", answer)
		
'''There are many flaws in the current code:  
	1. User can input strings and it will return an error.
	2. User can input float and it will return an error.
	3. User can enter duplicate numbers, and even though it provides the corrent 
	   response, it should ask the user to provide distinct numbers.
'''
