#!usr/bin/env python
## simple python script to lift all the $scopes and vars from a .js file

import sys
import re

fileString = str(sys.argv[1])

variables = set()

def storeLine(variable):
    variables.add(variable)

f = None
var_list = re.compile("[a-zA-Z0-9_]+[ ]?([::]|\()")
try:
    f= open(fileString, 'r')
    for line in f:
        foundVar = re.search(var_list, line)
        if foundVar:
            var = re.split(r'[::]|(\()', foundVar.group(0))
            if len(var[0]) > 2:
                storeLine(var[0].strip())
except:
    print("file not found")
finally:
     if f != None:
        f.close()

for variable in variables:
    print(variable)
