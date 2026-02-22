####### SETS METHODS ########

# C and update()
s1 = {1,2,3,3}
s2 = {4,5,6}
print("Union: ", s1.union(s2))
s1.update(s2)
print("Update(): ",s1) # s1 is updated

# Intersection() and intersection_update()

cities = {"Tokyo", "Madrid", "Berlin", "Niagra"}
cities2 = {"Manchester", "Tokyo", "Lahore"}
cities3 = {"Tokyo"}
print("Intersection(): ", cities.intersection(cities2))

# symmetric_difference() and symmetric_difference_update()
s5 = cities.symmetric_difference(cities2)
print("Symmetric_difference: ", s5)

# difference and difference_update()
s6 = cities.difference(cities2)
print("Difference: ", s6)

# isdisjoint()
print("isdisjoint(): ", cities.isdisjoint(cities2)) #false when there are including common values between 2 sets

# issuperset()
print("issuperset(): ", cities.issuperset(cities2)) #false because cities is not containing the values of cities2

# issubset()
print("issubset(): ", cities3.issubset(cities))

# add()
cities3.add("Peshawar")
print("Add(): ", cities3)

# Remove()/Discard()
s1.remove(5) # it will throw error because 8 is not present already. 
print("Remove(): ", s1)
s1.discard(8)
print("Discard(: ", s1) #it will not throw error if value is not present.
# but it doesnot mean that we will use discard() everytime, sometimes haveing an error is very necessary

# pop()
cities.pop() # it will pop/remove a random value, since sets are unordered
print("pop(): ", cities)

# del
# to delete an entire set, we use keyword "del", like below
city = {"Lahore", "Peshawar", "Islamabad", "Skardu"}
print("Before Del city: ", city)
# del city #it will throw error because there will be no set after deleting named "city"
print("After Del city: ", city)

# clear
# to just remove the values inside a set, we use the clear method
cars = {"Honda", "Corolla", "Suzuki"}
print("Before clear(): ", cars)
cars.clear()
print("After Clear(): ", cars)