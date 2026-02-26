########## MAP function ##########

l= [1,2,4,6,4,3,5]

newl = list(map(lambda x: x**3, l)) 
print(newl)

########## FILTER function ##########

def filter_func(x):
    return x>1

newl2 = list(filter(filter_func, l))
print(newl2)

########### REDUCE function ##########
# first we need to import reduce function from functools module
from functools import reduce

numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)
