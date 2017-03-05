# -*- coding: utf-8 -*-
import csv

class IrisReader:
    """
    A kinda-sorta rule of thumb is that if you see a Python class
    with a single function and an initializer
    then it probably shouldn't be a class at all.
    Ignore that in this case
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def open(self):
        try:
            f = open(self.file_path)
            my_file_data = csv.reader(f)
            return my_file_data
        except IOError:
            print("File not found\n")
            return None


class IrisStats:

    def __init__(self, file_path):
        self.sepal_length_column = 0
        self.petal_length_column = 2
        self.iris_data = None # this is set in each stats function

    def get_avg_petal_length(self):
        # TODO1: finish this function
        self.iris_data = IrisReader(file_path).open()
        if self.iris_data is not None:
            pass

    def get_avg_sepal_length_per_class(self):
        # TODO2: finish this function
        self.iris_data = IrisReader(file_path).open()
        if self.iris_data is not None:
            pass

import sys
iris_stats = IrisStats(sys.argv[1])
print(iris_stats.get_avg_petal_length())
