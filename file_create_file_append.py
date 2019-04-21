# Example of creating a file using append 
# If the file already exists it will add content to the end of the file

file = open("demofile_2.txt", "a")

file.write("Now there is more content\n")

file.close()