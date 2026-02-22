# TYPECASTING
# The conversion of one data type to another datatype is known as typecasting
# methods which are supported: int(), float(), str(), dict(), list(), ord(), hex(), tuple(), set()

# 2 types
# * Explicit typecasting (in which developer is willing to convert the datatype into another)
# * Implicit typecasting (if one datatype is int and other is float, the result will be float)

a=1
b=2
print(a+b)

a="1"
b="3"
# if we print simple using a+b, it will give error because now a and b contains strings
# but it is possible to still perform the operation
print(int(a) + int(b)) #this is explicit typecasting

a = 1.1
b = 7
print(a+b)