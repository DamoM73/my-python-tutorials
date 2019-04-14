# Example of how to open a file and read parts of it.

file = open("demofile_1.txt","r")

print(file.read(6))
print(file.read())

file.close()
