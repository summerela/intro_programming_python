#import sys
import csv
#import os

Rus_ports_nos = []
Aus_ports_nos = []
Other_countries = []

in_file = open("./airports.dat", "r", encoding='utf-8')

#the following reads through the input file and creates new variable lists with just the
#Australia and Russia data in it.
for line in in_file:
    line = line.strip()
    parts = line.split(",")
    if parts[3] == '"Russia"':
        Rus_ports_nos.append(parts)
    elif parts[3] == '"Australia"':
        Aus_ports_nos.append(parts)
    else:
        Other_countries.append(parts[3])

print("The data for Russian airports listed are {}.\n \
    The airports listed in Australia are {}.".format(Rus_ports_nos,Aus_ports_nos))

print ("There are {} Russian airports listed, {} Australian airports listed, \
    and {} other countries airports listed.".format(len(Rus_ports_nos),len(Aus_ports_nos),len(Other_countries)))

in_file.close()
