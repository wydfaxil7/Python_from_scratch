with open("seek.txt", "r") as f:
    print(type(f))

    f.seek(10) #it will move to the 10th byte in the file
    print(f.tell()) # it will return the current position of the file pointer

    data = f.read(5) # it will read the next 5 bytes 
    print(data) 

with open("truncate.txt", "w") as f:
    f.write("This is a sample text for truncating the file.")
    f.truncate(20) # it will truncate the file to 20 bytes
