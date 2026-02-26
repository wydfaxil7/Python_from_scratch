############ LAMBDA FUNCTION ############

# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments: expression

cube = lambda x: x**3
avg = lambda x,y,z: (x+y+z)/3

print(cube(3))  
print(avg(10,20,40))

# also we can use it inside any function

# example
def apple(fx, value):
    return 6 + fx(value)
print(apple(cube, 3))
print(apple(lambda x: x*x, 2))