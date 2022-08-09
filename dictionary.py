myDict = {"name": "stephen", "age": 22,
          "address": "nashville", "school": "fisk"}

myDict["age"] = 25

del myDict["school"]  # To delete an item - you can use pop() too

print(myDict)


def transverseDict(dict):
    for key in dict:
        print(key, dict[key])


# transverseDict(myDict)

# Copy method in dictionary

# newDict = myDict.copy()
newDict = {}.fromkeys([1, 2, 3], 0)

newDict["nick"] = "peach"

# print(newDict)
# print(myDict.items())
# print(myDict.keys())
print(myDict.setdefault("jam", "added"))

print(myDict)
rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
id1 = id(rec)
del rec
rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
id2 = id(rec)

print(id1 == id2)
print(id1, id2)

# Tuples

newTuple = "a", 'b', 'c', 'd', 'e'
newTuple1 = ('a',)
newTuple2 = tuple(rec.values())
print(newTuple2)

# Methods that cannot be used for tuples - append(), insert(), remove(), pop(), clear(), sort(), reverse()
# Tuples can be stored in a list and list can be stored in a tuple

init_tuple = ()
print(init_tuple.__len__())

init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]
