import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(1, 100):
    os.rename(f"data/day{i}", f"data/fazil{i}") # Renames each folder from "day1", "day2", ..., "day99" to "fazil1", "fazil2", ..., "fazil99" in the "data" directory.