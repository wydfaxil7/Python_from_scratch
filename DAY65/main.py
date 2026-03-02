########## STATIC METHOD ##########


class Math:
    @staticmethod # these method are often used to make the utility functions
    def add(a,b,c):
        return a+b+c
    
    @staticmethod
    def subtract(a,b):
        return a-b
    
print(Math.add(1,4,2)) # the static method can be called without creating an instance of the class.
print(Math.subtract(5,2))

# print(add(1,2,3))