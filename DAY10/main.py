# Taking input

a = input("Enter your name: ")
print(a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x + y) #this is concatenation, the python compiler is understanding x & y as strings

# So for adding the numbers, we have to convert them into strings.
print(int(x) + int(y))