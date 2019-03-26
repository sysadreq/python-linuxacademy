colors = ["blue", "green", "red", "purple"]

# for TEMP_VAR in SEQUENCE:
for color in colors:
    print(color)


for color in colors:
    if color == "blue":
        continue
    elif color =="red":
        break
    print(color)

#tuples
point = (2.1,3.2,7.5)
for value in point:
    print(value)

#dictionaries
ages = {"kevin":59,"bob":40,"kayla":30}
for key in ages:
    print(key)

#string
for letter in "ronn_anthony":
    print(letter)


#unpacking variables
list_of_points = [(1,2),(3,4),(5,6)]
for x,y in list_of_points:
    print(f"x: {x}, y: {y}")


#dictionary.items()
for name, age in ages.items():
    print(f"Person Named: {name}")
    print(f"Age of: {age}")
