############# FUNCTION ARGUMENTS #############
# There are several types of function arguments. so we will def them below 

############## 1. Default Arguments ##############

# def Average(a=3, b=7): #default values given
#     avg = (a+b)/2
#     print("The average is: ", avg)

# Average()

############## 2. Keyword Arguments ##############

# def Average(a, b):
#     avg = (a+b)/2
#     print("The average is: ", avg)

# Average(10,2)


############## 3. Required Arguments ##############

# def Average(a, b=3): #here a is a required argument
#     avg = (a+b)/2
#     print("The average is: ", avg)

# Average(10, 10) # but if i provide the default parameter too here, it will print the new, without a parameter, it iwll throw error 

############## 4. Variable Length Arguments ##############

# def Average(*numbers):
#     sum = 0 
#     for i in numbers:
#         sum = sum + i
#         avg = sum/len(numbers)
#     print("The average is: ", avg)

# Average(1,4,6,2,5,2)


############## 5. Keyword Arbitrary Arguments ##############

# def name(**name): #here name is taken as dictionary
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")


#### RETURN STATMENT
# it ois used to return the value back to the calling function

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))