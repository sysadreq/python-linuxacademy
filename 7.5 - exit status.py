import argparse
import sys

# build the parser
parser = argparse.ArgumentParser(description="Read a file in reverse")
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit','-l', type=int, help='the number of lines to read')
parser.add_argument('--version','-v', action='version', version='%(prog)s v1.0')

args=parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except:
    print(f'File not found Error: {args.filename}')
    sys.exit(2) #print an exit status
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
                lines = lines[:args.limit]

        for line in lines:
                print(line.strip()[::-1])
finally:
    print("finally")