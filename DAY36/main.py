########### exception handling ############

# a = input("Enter a number: ")
# print(f"\nMultiplication table of {a} is: ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("!!!!!!!INVALID ERROR OCCURED!!!!!!!!")

# Also we can make multiple exceptions like below

try: 
    num = int(input("Enter a number: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("VALUE ERROR: Not an integer!!!!!!!!")
except IndexError:
    print("Index Error!!!!!!!!!!")



print("\nIS IT HANDLING EXCEPTIONS????")
