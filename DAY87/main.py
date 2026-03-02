######### walrus operator #########

# example with classic

foods = list()

# while True:
#     food = input("Enter a food: ")
#     if food == "quit":
#         break
#     foods.append(food)   # writing this way is correct too, but we can do it better with walrus operator  

# while (food :=input("Enter a food: ")) !="quit":
#     foods.append(food)

numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(f"There are {n} numbers in the list.")
    numbers.pop()


    