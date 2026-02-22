import time


timezone = time.strftime('%H:%M:%S')
print("TIME: ", timezone)

# timezone = time.strftime('%H')
# print(timezone)

# timezone = time.strftime('%M')
# print(timezone)

# timezone = time.strftime('%S')
# print(timezone)


######### EXCERCISE ##########
# create a python program capable of greeting you with GOOD MORNING, GOOD AFTERNOON, GOOD EVENING. 

hour = int(time.strftime('%H'))

if(hour >= 5 and hour < 12):
    print("GOOD MORNING, FAZIL. Have a nice day.")
elif(hour >= 12 and hour < 17):
    print("GOOD AFTERNOON, FAZIL. Dont forget to eat your lunch")
elif(hour >= 17 and hour < 21):
    print("GOOD EVENING, FAZIL. Have a good dinner")
else:
    print("GOOD NIGHT. Sweet dreams, FAZIL.")