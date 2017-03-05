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
        # TODO3: instead of reading
        # the file in everytime
        # is there a way to read it in once
        # and if it was already read, return
        # the existing file data?
        try:
            f = open(self.file_path)
            my_file = csv.reader(f)
            return my_file
        except IOError:
            print("File not found\n")
            return None


class IrisStats:

    def __init__(self, file_path):
        self.sepal_length_column = 0
        self.petal_length_column = 2
        self.iris_data = IrisReader(file_path).open()

    def get_avg_petal_length(self):
        # TODO1: write this function
        pass

    def get_avg_sepal_length_per_class(self):
        # TODO2: write this function
        pass

import sys
iris_stats = IrisStats(sys.argv[1])
print(iris_stats.get_avg_petal_length())
