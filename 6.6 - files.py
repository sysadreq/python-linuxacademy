#reading a file
xmen_file=open('xmen_base.txt','r')

xmen_file.read()

xmen_file.seek(0)

for line in xmen_file:
    print(line, end="")
xmen_file.close()


#writing/copying a file
xmen_file=open('xmen_base.txt','r')
new_xmen=open('new_xmen.txt','w')
new_xmen.write(xmen_file.read())
new_xmen=open(new_xmen.name,'r+')

for line in new_xmen:
    print(line, end="")
new_xmen.seek(0)

#add a new word replacing whatever is in the current cursor position
new_xmen.write("Beast\n")
new_xmen.write("Phoenix\n")
new_xmen.seek(0)

for line in new_xmen:
    print(line, end="")
new_xmen.close()
xmen_file.close()