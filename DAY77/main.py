############ OPERATOR OVERLOADING ############

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __mul__(self, x):
        return Vector(self.i * x.i, self.j * x.j, self.k * x.k)
    
v1 = Vector(3, 2, 6)
print(v1)
v2 = Vector(1, 5, 7)
print(v2)
Result = v1 * v2
print (Result)
print(type(Result))