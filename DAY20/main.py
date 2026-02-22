# Funtions
# There are two types of functions
# 1. Built-in functions
# 2. user defined functions


def GeometricMean(a,b):  # define the function first so we can use it multiple times
    mean = (a*b)/(a+b)
    print(mean)

a=8
b=6
# GeometricMean(a,b)

c=5
d=9
# GeometricMean(c,d)

e=4
f=2
# GeometricMean(e,f)

def isGreater(a,b):
    if (a>b):
        print(a, "is greater")
    elif (a == b):
        print(a, "and", b, "are equal")
    else:
        print(b, "is greater")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
isGreater(a,b)