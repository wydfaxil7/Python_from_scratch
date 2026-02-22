# Strings are immutable

a = "!!Fazil @!!! Fazil 888 Fazil"
print(len(a))
print("UPPER:",a.upper())
print("LOWER", a.lower())

print("STRIPPED: ", a.rstrip("!")) 
# strips the trailing character 

# print(a.rstrip("!")) 
# But it will not strip the leading character, only trailinh characters

print("REPLACED", a.replace("Fazil", "John")) 
# it replaces all occurences

print("SPLIT", a.split(" ")) 
# it splits the string at whitespaces

Blog = "introduction tO JS and pYthon."
print("CAPITALIZED: ", Blog.capitalize())
# it capitalize the first character and not the other. if other are in capital, they will not be.

str2 = "Welcome to the blog"
print("CENTER: ", len(str2))
print(len(str2.center(100)))
print(str2.center(100, '.'))
# aligns the string to the center as per parameter value.

print("COUNT: ", a.count("Fazil"))
# Counts the number of times the given parameter has occurred

b = "Welcome to the Blog !!!"
print("ENDSWITH 1: ", b.endswith("!!!")) # if the string is ending with the given parameter, it returns true, else false
print("ENDSWITH 2: ", b.endswith("@@@"))
print("ENDSWITH 3: ", b.endswith("Blog", 4,10))
print("STARTSWITH: ", b.startswith("We"))


print("FIND: ", b.find("to"))
# finds the index of given parameter
# print("INDEX: ", b.index("ish")) # it will throw error if not found
print("INDEX 2: ", b.index("to")) # it will not throw error if not found

# "isalnum()" method says true if sting contains A-Z or a-z or 0-9
# "isalpha()" method says true if sting contains A-Z or a-z
# "islower()" method says true if sting contains lowercase characters
# "isupper()" method says true if sting contains uppercase characters
# "isprintable()" method says true if sting contains printable characters, nonprintable like '\n'
# "isspace()" method says true if the string has spaces, either spacebar or tab spaces
# "swapcase()" converts lowercase to uppercase and vice versa

string = "World Health Organization"
print("TITLE: ", string.istitle())
string2 = "To kill a mockingbird"
print("TITLE: ", string2.istitle())
print("titlecase", string2.title()) # it makes the first character of each word capital.
# istitle() says true if first character of each world is capital, else false


############## THESE ARE THE METHODS BELOW USED ABOVE ##############
# upper

# lower

# rstrip

# replace

# split

# capitalize

# center

# count

# endswith

# startswith

# find

# index

# isalnum

# isalpha

# islower

# isupper

# isprintable

# isspace

# swapcase

# istitle

# title