######### LIST METHODS ###########

l = [1,4,2,11,6,7,1,2]
print("ORIGINAL LIST: ", l)
# l.append(8)
# l.sort()
# l.sort(reverse=True) # sort in descending
# l.reverse() #Reverse the original list
# print(l.index(1))
# print(l.count(1))
# print("CHANGED LIST: ", l)


############ TUPLES ############
# Tuples are immutable too. comparing it with list, list can be changed, but we are unable to change the tuple

tup = (1,2,3,7,5,2,1, "green", True) 
# tup = (1) # if we does not use, the python interpreter will consider it as class int 
# print(type(tup), tup)
# print(len(tup))
# print(tup[0])
# print(tup[2])
# print(tup[-1])
# print(tup[-4])

# if 3421 in tup:
    # print("YES, 3421 is in the tuple")
# tup2 = tup[1:4]
# print(tup2)


################ OPERATIONS IN TUPLE ################
# we cannot change the existing tuple, unless is changed temporarily as list.

countries = ("Nepal", "Pakistan", "Austrailia", "USA", "China", "Iran")
# temp = list(countries) #convert tuple into list
# temp.append("Russia")   #add item
# temp.pop(3)             #remove item
# temp[2] = "Finland"     #replace item
# countries = tuple(temp)
# print(countries)

# also we can concatenate two tuples and it will a new tuple
countries2 = ("Vietnam", "Japan")
# newCountries = countries + countries2
# print(newCountries)


############# TUPLE METHODS ##########

# count()
Tuple1 = (1,2,3,2,1,4,5,3,6,7,32)
# res = Tuple1.count(3)
# print("Countof 3 in Tuple1 is: ", res)

# res = Tuple1.index(3)
res = Tuple1.index(3, 4, 8)
print(res)