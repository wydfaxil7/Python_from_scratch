########### ENUMERATE FUNCTION ##########
# used to loop over something and get both the index and value

colors = ["Orange", "Yellow", "Blue", "Red"]

for index, i in enumerate(colors, start = 1):
    print(f'{index}: {i}')