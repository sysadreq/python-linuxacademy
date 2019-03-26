#lists

my_list = [1,2,3,4,5,6]
print(my_list)

print(my_list[0])
print(len(my_list))

#slice
#[starting index, ending index, step value]
print(my_list[0:2])

print(my_list[1::2])

print(my_list[:3])

#reassign
my_list[0] = "a"
print(my_list)

#add a new item to the list
my_list.append(6)
my_list.append(7)
print(my_list)


my_list += [8,9,10]
print(my_list)

my_list[2:3] = ["b","c"]
print(my_list)

#test if list element is an integer
for num in my_list:
    if isinstance(num, int):
        print('hello')


my_list2 = ["a","b","c"]
print(my_list2)
