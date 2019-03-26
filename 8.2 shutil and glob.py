import os
import glob
import json
import shutil

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directly already exist")


receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split("/")[-1]
    destination = f'./processed/{name}'
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print('Receipt subtotal: $%.2f' % subtotal)


'''
glob.glob(pathname, *, recursive=False)
Return a possibly-empty list of path names that match pathname, which must be a string containing a path specification.


We used the json.dump function to write out a JSON file, and we can use the opposite function json.load to read a JSON file. The contents of the file will be turned into a dictionary that we can us to access its keys. 
We’ll add the value to the subtotal before finally moving the file using shutil.move.
'''

