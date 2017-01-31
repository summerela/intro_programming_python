# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys

def print_args(*args):
    for index, arg in enumerate(*args):
        print("[ ARG-{} ]: {}".format(index, arg))

#
# using the sys module to list
# the extra arguments passed to a script
#
print_args(sys.argv)

