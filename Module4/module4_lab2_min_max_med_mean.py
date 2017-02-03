# -*- coding: utf-8 -*-
#!/usr/local/src python3

import os, sys
ABSOLUTE_TSV_PATH=os.path.join( os.path.split(os.path.abspath(__name__))[0], 'data', 'fahrenheit_monthly_readings.tsv' )

def get_max_width(table, padding=2):
    #calculate the max width of the table cell
    max_width = 0
    for row in table[1:]: # skip the header row:
        new_max = max([len(value) for value in row]) + padding
        # only set the new max if it's actually greater
        if new_max > max_width:
            max_width = new_max
    return max_width

def print_table(table):
    max_width = get_max_width(table)
    for row in table:
        print(*[str(i).center(max_width) for i in row], sep='|')

def calc_max_temp_average(table):
    max_temps = []
    for row in table[1:]: # skip the header row:
        max_column = len(row) - 1
        max_temps.append(int(row[max_column])) 

    print("[ AVERAGE MAX TEMP ]: {}".format(sum(max_temps)/len(max_temps)))

def calc_min_temp(table):
    min = None
    for row in table[1:]: # skip the header row:
        min_column = len(row) - 2
        new_min = int(row[min_column]) 

        if min is None: # indicator to set first min value
            min = new_min

        if new_min < min:
            min = new_min

    print("[ MIN TEMP ]: {}".format(min))

def calc_max_temp(table):
    max_temps = []
    for row in table[1:]: # skip the header row:
        max_column = len(row) - 1
        max_temps.append( int(row[max_column]) )

    print("[ MAX TEMP ]: {}".format(max(max_temps)))

def calc_median_temp(table):
    import statistics
    all_temps = []
    for row in table[1:]: # skip the header row:
        min_column = len(row) - 2
        max_column = len(row) - 1
        all_temps = all_temps + [ int(row[min_column]), int(row[max_column]) ]

    print("[ MEDIAN OF ALL TEMPS ]: {}".format(statistics.median(all_temps)))

in_memory_table = []
with open( ABSOLUTE_TSV_PATH, 'r' ) as file_sock:
    for line in file_sock:
        line = line.strip() # strip off extraneous whitespace chars such as newline or tabs
        row = line.split('\t')
        in_memory_table.append(row)

# RUN THIS THANG
print_table(in_memory_table)
calc_max_temp_average(in_memory_table)
calc_max_temp(in_memory_table)
calc_min_temp(in_memory_table)
calc_median_temp(in_memory_table)




