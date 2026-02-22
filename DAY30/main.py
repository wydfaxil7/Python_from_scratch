########## RECURSION ###########
# calling a function inside a function


# def factorial(num):
#     if(num == 1 or num == 0):
#         return 1
#     else:
#         return(num * factorial(num - 1))

# num = 3
# print("Number: ", num)
# print("Factorial: ", factorial(num))

# Fibonacci Sequence
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fib = int(input("Enter your number: "))

for i in range(fib):
    print(fibonacci(i), end=" ")

