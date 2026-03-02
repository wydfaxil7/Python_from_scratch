import os

files = os.listdir("Clutter")
i = 1
for file in files:
    if file.endswith(".txt"):
        print(file)
    os.rename(f"Clutter/{file}", f"Clutter/{i}.png")
    i = i+1

# this will be only changing the files which are ending with .txt and changing the name to 1.png, 2.png, 3.png and so on.