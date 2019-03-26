import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

args = parser.parse_args()
snippet = args.snippet.lower()

#open /usr/share/dict/words and assign it to variable file
with open('/usr/share/dict/words') as file:
    words = file.readlines() # read the file and put it in a list

'''
matches = []

#iterate from the list 'words', if it matches, append to 'matches' list
for word in words:
    if snippet in word.lower():
        matches.append(word)
'''

#list comprehension
matches = [word.strip() for word in words if snippet in word.lower()]

print(matches)
