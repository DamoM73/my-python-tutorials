# Example of how to open a file and loop through reading each line

file = open("demofile_1.txt","r")

for line in file:
    print(line)

file.close()