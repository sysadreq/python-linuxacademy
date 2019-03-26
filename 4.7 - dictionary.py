#dictionary

ages = {'kevin':59, 'alex':29, 'bob':40}
print(ages)

#getting a value
print(ages['kevin'])


#adding a key and value
ages['kayla'] = 21
print(ages)

ages['kayla'] = 22
print(ages)


#removing a key and value
del ages['kevin']
print(ages)

#pop
ages = {'kevin':59, 'alex':29, 'bob':40}
ages.pop('alex')
print(ages)

#get all the keys
print(ages.keys())
#make a list
print(list(ages.keys()))

#get all the values
print(ages.values())
#make a list
print(list(ages.values()))

weights = dict(kevin=160, john=120, kayla = 135)
print(weights)


colors=dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors)


print(4*"1.1")