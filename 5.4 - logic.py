#logic

name = ""

#not is a logic operation
if not name:
    print("no name given")


#or logic operation
first = ""
last = ""

if first or last:
    print("the user has a first or lastname")

last = ""
last_name = last or "Doe"
print(last_name)


#and logic operations
first = "keith"
last = ""

if first or last:
    print(f"the user has a first or last name, {first} {last}")
elif first:
    print(f"first name: {first}")
elif last:
    print(f"last name: {last}")