# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
import argparse

def print_args(*args):
    print("[ ARGS ]: {}".format(args))

#
#  best option is to use `argparse` module
#
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='Enable `foo` checking with this flag', action='store_true')
parser.add_argument('--bar', help='The number of `bar`s in your program', type=int, choices=[1,2,3], required=True)
parser.add_argument('--baz', help='A list of `baz`s in your program', nargs='+', required=True)

# get the arguments passed to the command line
args = parser.parse_args()

# note: they are part of a  `Namespace` object
print_args( args )

# access the arguments passed to the command line
if args.foo is True:
    print("[ FOO ]: {}".format(args.foo))
else:
    print("[ FOO ]: False")

print("[ BAR ]: {}".format('Bar ' * args.bar))

print("[ BAZ LIST ]: {}".format(args.baz))
