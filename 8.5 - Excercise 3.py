#Excercise 4

#!/usr/bin/env python3.6

import argparse

parser = argparse.ArgumentParser(description="Handling file errors when files doesn't exist")
parser.add_argument('-f','--filename',help='input a filename')
parser.add_argument('-l','--line_number',help='input a line number')
args=parser.parse_args()


try:
    f = open(args.filename)
    sline = (int(args.line_number) - 1)
except:
    print('file not found!')
else:
    if sline < 0:
        print('line cannot be 0')
    else:
        list1 = f.readlines()
        print(list1[sline].strip())

