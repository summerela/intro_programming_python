#!/usr/bin/env python3

import sys
import csv

def read_in_csv(file_path):
    f = open(file_path)
    my_file = csv.reader(f)
    return my_file

def get_column_unique(in_file, col_number):
    col_list = []
    my_file = read_in_csv(in_file)
    for row in my_file:
        col_list.append(row[col_number])
    unique_vals = set(col_list)
    unique_length = len(unique_vals)
    return unique_length    

def count_things(in_file, col_number):
    my_dict = {}
    my_file = read_in_csv(in_file)
    
    # loop through dictionary to track name and count
    for row in my_file:
        key_name = row[col_number]
        
        # for every row, check if the class_name is in the dictionary
        if key_name in my_dict:
            my_dict[key_name] = my_dict[key_name] + 1
        
        # if not, add it, and set the count to 1
        else:
            my_dict[key_name] = 1
    
    return my_dict

unique_vals = get_column_unique("./iris.csv", 3)
count_classes = count_things("./iris.csv", 3)

print(unique_vals)
print(count_classes)