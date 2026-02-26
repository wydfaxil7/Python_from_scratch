import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/day{i+1}") # Creates a folder for each day from 1 to 99 in the "data" directory.