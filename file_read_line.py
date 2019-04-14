# Example of how to open a file and read a line of the file

file = open("demofile_1.txt","r")

print(file.readline())
print(file.readline())

file.close()