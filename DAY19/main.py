# BREAK and CONTINUE

# break makes you exit the loop
# continue makes you exit the iteration

# print("########## BREAK STATEMENT ##########")
# for i in range(14):
#     if(i==15):
#         break
#     print("5 X ", i+1, "=", 5*(i+1))

# print("THE LOOP IS BROKEN")

# print("\n########## BREAK STATEMENT ##########")

# for i in range(12):
#     if(i==7):
#         print("THE ITERATION IS SKIPPED")
#         continue
#     print("5 X ", i, "=", 5*i)


# Emulating DO WHILE loop

i = 0
while True:
    print(i)
    i = i + 1
    if(i%50 == 0):
        break