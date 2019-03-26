import argparse

# build the parser
parser = argparse.ArgumentParser(description="Read a file in reverse")
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit','-l', type=int, help='the number of lines to read')
parser.add_argument('--version','-v', action='version', version='%(prog)s v1.0')

args=parser.parse_args()

# read the rile, reverse the contents and print


#try and open the file, else print and error
try:
    f = open(args.filename)
    limit = args.limit
#except FileNotFoundError as err:
except:
    print(f'File not found Error: {args.filename}')
else:
    with f:
#append the contents to a list
        lines = f.readlines()
#reverse the arrangement of the list, last element will be first and so on.
        lines.reverse()

#limit the elements to be reversed
        if args.limit:
                lines = lines[:args.limit]

#reverse the characters in each element
        for line in lines:
                print(line.strip()[::-1])
finally:
    print("finally")