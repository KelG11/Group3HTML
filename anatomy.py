#!/usr/bin/python

# Example python script

import sys # The sys module provides information about constants, functions and methods of the Python interpreter.

argc = len(sys.argv)

if argc > 1:
    print("Too many args")
else:
    where = ("World")
    print("Hello", where)

print("Goodbye from"+sys.argv[0])

# By using the IF condition function we are able to change the outcome printed within the script.
# When IF is changed to 0 the argument run is too many args
# Else function is run when the function is changed to 1

