########### f-strings ##############

#String formatting can be dont using the format method

txt = "For only {price:.2f} dollars"
print(txt.format(price=69.09999))


val = "Geeks"
print(f"{val} for {val} is a portalfor {val}")
name = "Fazil"
Country = "Pakistan"
print(f"Hey! My name is {name} and I am from {Country}")


# also we can use f-strings in a single statment
print(f"{2*40}")


############## docstrings ##############

def Square(n):
    '''This will calculate the square of a number n''' # the rule is that the statement should always be right after defining the function in " ''' ''' " otherwise it will show None
    print("The square is: ", n**2)

Square(7)
print(Square.__doc__) # this is the format of the docsting


import this
# this will print the poem for PEP-8