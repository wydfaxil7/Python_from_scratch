# lists

marks = [10,20,30,"Fazil",True]
print(type(marks))
# print(marks[4])
# print(marks[2])
# print(marks[3])
# print(marks[-4])
# print(marks[-2])
# print(marks[-3])

color = ["Red", "Green", "Yellow", "Blue", "White"]
# # if "Green" in color:
# if "Black" in color:
#     print("YES<  is in list")
# else:
#     print("NO< Black is not in list")


########## RANGE OF INDEX IN LIST ##########

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'
# print(animals[3:])
# print(animals[-5:])
# print(animals[:3])
# print(animals[:-6])
# print(animals[::2]) #printing alternate values
# print(animals[:8:3])


########## LIST COMPREHENSION ##########

names = ["Milo", "Rosa", "Anastasia", "Mark", "Jack", "Sarah"]
# namewith_o = [i for i in names if "o" in i]
# print(namewith_o)
grt4 = [i for i in names if (len(i) > 4)]
print(grt4)