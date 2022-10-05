# Handling files
# Last update: 25/07/2019


import os

# Define the working location and change to that location. Otherwise the work will be done by default in C:/Users/UCD.
working_location = "C:/Users/UCD/Desktop"
os.chdir(working_location)

# Open a file for writing (w) and create a new if it doesn't exist (+).
open_file_to_write = open("file_1.txt", "w+")

# Write the following on the file.
open_file_to_write.write("\nThis is the title\n\n")

# Loop and write the following i times.
for i in range(5):

    # %d acts as a place holder for values, %s would do same for strings. Would be same as the f"string{whatever}string".
    open_file_to_write.write(f"this is line %d\n" % (i + 1))

# Write some
ask_thigs = input(str("write something here: \n"))
open_file_to_write.write(f"this inside brakets ({ask_thigs}) has been asked by keyboard\n")

# Close the file.
open_file_to_write.close()


# Same for appending, use (a) instead of w.
open_file_to_append = open("file_1.txt", "a+")

for i in range(3):
    open_file_to_append.write(f"this is appended line {i + 1}\n")
open_file_to_append.close()

# Same for reading, use (r).
open_file_to_read = open("file_1.txt", "r")
print(open_file_to_read.read())


#shutil.move("C:/Users/UCD/file4.txt", "C:/Users/UCD/Desktop")
#os.rename("C:/Users/UCD/file4.txt", "C:/Users/UCD/Desktop")
