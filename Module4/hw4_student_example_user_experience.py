#!/bin/env python

import csv

#converting file to csv format
airports = open("./airports.dat.txt")
readairports = csv.reader(airports)

#set initial counter for russian & aussie airports to 0
russia = 0
auz = 0

#loop searches for russian and australian airports and prints them out
#also russian & aussie airport counter increases by 1
for location in readairports:
    if location[3] == "Australia":
    	#limited index range to clean up data and redundant info
        print(location[0:9])
        auz += 1
    elif location[3] == "Russia":
    	 #limited index range to clean up data and redundant info
        print(location[0:9])
        russia += 1
    else:
    	#skips row if no match for russian & australian airports
        continue

#printing totals from completed for loop of russian & australian airports    
print("There are {} russian airports.".format(russia))
print("There are {} australian airports.".format(auz))

airports.close()
