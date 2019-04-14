'''
Example of creatinga file using write and writing to the file
If the file already exists it will replace the content of that file.
'''

file = open("demofile_2.txt", "w")

file.write("This is the new content for the file.\n")
file.write("I hope you like it\n")

file.close()