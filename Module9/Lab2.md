# Module 9 Lab 2

We love iris flowers in this class. Let's return to the [iris.csv](https://github.com/summerela/intro_programming_python/blob/master/Module6/iris.csv) dataset in this lab and try to write our simple statistics
inside classes.

## Instructions:

0. Copy `lab2.py` to your workspace

0. Look for `TODO1` in the code. Can you finish writing this function without accessing any variables outside of the `IrisStats` class?

0. Look for `TODO2` in the code. Can you finish writing this function without accessing any variables outside of the `IrisStats` class?

0. The final TODO is a little harder to explain. The idea is that we don't want to read the csv for every statistical function we write because it's repetative. There should be multiple ways to refactor the code to read the file once and cache the `self.iris_data` read from the csv. This can be done in the `IrisReader` or `IrisStats` class. So you have options.
