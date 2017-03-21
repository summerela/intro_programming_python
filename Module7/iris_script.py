#!/usr/bin/env python3

import sys
import csv
import sys

my_file = sys.argv[1]

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

# calc average of a column
def average_col(in_file, col):
    my_file = read_in_csv(in_file)
    vals_to_avg = []
    for row in my_file:
       vals_to_avg.append(float(row[col]))
    col_sum= sum(vals_to_avg)
    length = len(vals_to_avg)
    avg = col_sum/length
    return avg

# calc averge of specific class
def calc_class_avg(infile, class_col, class_name):
    my_file = read_in_csv(infile)
    vals_to_avg = []
    
    # loop through dictionary to track name and count
    for row in my_file:
        if row[class_col] == class_name:
           vals_to_avg.append(float(row[0]))
    val_sum =sum(vals_to_avg)
    val_length = int(len(vals_to_avg))
    class_avg = val_sum/val_length
    return class_avg

# get petal length for a particular class
# feed it file
# petal length column  number
# class column number

def calc_class_avg(infile, avg_col, class_col, class_name):

    petal_length_list = []

    # read in the file
    my_file = read_in_csv(infile)

    # if class col is equal to the class name
    for row in file:
        if row[class_col] == class_name:
            petal_length_list.append(row[avg_col])

    # get the petal length

    # sum petal

    # divide that by how many observations


# have the user specify input file
in_file = sys.argv[1]

unique_vals = get_column_unique(my_file, 4)
count_classes = count_things(my_file, 4)

#calculate overall average sepal length
sepal_avg = average_col(in_file,0)


# calculate average sepal length by class name
sepal_class_length = calc_class_avg(sys.argv[1], 4, "iris-setosa")

print("There are {} unique classes in this file.".format(unique_vals))
print(count_classes)
print(sepal_avg)
print(sepal_class_length)
