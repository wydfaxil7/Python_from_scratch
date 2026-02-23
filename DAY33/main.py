########## PYTHON DICTIONARIES ##########

info = { 
'name': 'Fazil',
'age': 23,
'country': 'Pakistan',
'eligible': True
}


# 1. accessing one value
print(info['name']) #if the key is not present in the dictionary, then it will show an error
# print(info['song']) # like this
print(info.get('country'))
print(info.get('song')) # if value is not present, it will not throw an error, but will show "none"

# 2. accessing multiple values
print(info.values())

# 3. Accessing keys
print(info.keys())

# 4. Accessing key value pairs
# print(info.items())
for key, value in info.items():
    print(f"The corresponding value to the key {key} is {value}")


########### DICTIONARY METHODS ############

print("\n METHODS \n")
ep1 = {
    120: 45,
    121: 67,
    122: 69,
    123: 83,
    124: 43
}

ep2 = {
    125: 78,
    126: 34,
    127: 37
}
# .1 update()
ep1.update(ep2)
ep1.update({'Fazil': 'Cool'})
print("Update(): ", ep1)

# .2 Remove
ep3 = {
    125: 78,
    126: 34,
    127: 37
}
ep3.clear()
print("Clear(): ", ep3)

# .3 pop()
ep1.pop(122)
print("pop(): ", ep1)

# .4 popitem()
# it removes the last item in dictionary
ep2.popitem()
print("popitem(): ", ep2)

# .5 del
# del ep1 # will throw error if i will print it
print(ep1)

