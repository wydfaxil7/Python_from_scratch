########### DECORATORS ############
# decorators is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.

# def decorator_function(ogfunction):
#     def wrapper_function():
#         print("This is the wrapper function")
#         ogfunction()
#     return wrapper_function
# @decorator_function
# def display():
#     print("This is the original function")
# display()

def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@simple_decorator
def add(a,b):
    print(a+b)

add(5,10,20)

# i dont understand it.