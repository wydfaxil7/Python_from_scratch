######## FILE HANDLING ########

# Creating/writing a file
# f = open("fazil.txt", "w")
# f.write("Hello, i am testing this file handling in python")
# f.close()

# Reading a file
# f = open("fazil.txt", "r")
# print(f.read())
# f.close()

# Appending to a file
# f= open("fazil.txt", "a")
# f.write("\nI have appended this in file")

# but if we see, writing code like this or accessing files like this is very much time consuming

# with open("fazil2.txt", "w") as f: 
#     f.write("This is a new file created using 'with' statement.")
# Creating a file


# with open("fazil2.txt", "r") as f:
#     content = f.read()
#     print(content)
# Reading a file


# with open("fazil2.txt", "a") as f:
#     f.write("\nThis line is appended to the file.")
# Appending to a file



# readline()
f = open("fazil.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line, type(line))

# writelines()
f = open("fazil.txt", "w")
lines = ["line 1\n", "line 2\n", "line 3\n"]
f.writelines(lines)
f.close()