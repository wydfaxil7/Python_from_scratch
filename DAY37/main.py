# use of "Finally" in exception handling

# try:
#     l = [1,5,7,3]
#     i = int(input("Enter the index: "))
#     print(l[i])
# except: 
#     print("SOME ERROR OCCURED!")

# # finally:
# #     print("\nI WILL ALWAYS BE EXECUTED")
# print("\nI WILL ALWAYS BE EXECUTED") # this is going to be executed too. but the difference when making a function



# def func1():
#     try:
#         l = [1,5,7,3]
#         i = int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except: 
#         print("SOME ERROR OCCURED!")
#         return 0

#     finally:
#         print("\nI WILL ALWAYS BE EXECUTED")
# # print("\nAM I STILL EXECUTABLE?!") # this is going to be executed too. but the difference when making a function

# x = func1()
# print(x)





# ALSO WE CAN RAISE CUSTOM ERRORS USING "raise" KEYWORD
user_input = input("Enter number between 5 and 9 (or type 'Quit' to exit):")
if user_input.lower() == "quit":
    print(f"You typed {user_input}.So you have quit ")
else:
    try:
        num = int(user_input)
        if num > 9 or num < 5:
            raise ValueError("Value should be between 5 and 9")
        else:
            print(f"You entered {num}")
    except Exception as e:
        print("Error:",e)
