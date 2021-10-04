'''
Goal: Give the python code a location on my computer to look for #TODO.
If found, it copies/writes the line to a TODO.txt file.
Step 1: Write some python so I can give a specific location to look through.
Step 2: Loop through all the files/folders in that location.
Step 3: copy each line with a #TODO to a TODO.txt
'''

import os
import datetime
import sys

print(sys.version)
print("len argv", len(sys.argv), " argv: ", sys.argv)

# Pathway to folder I want to look through.

rootdir = os.getcwd()
print(rootdir)
# '/Users/chandlerkilpatrick/.julia/dev/SHERPA'

# Pathway to file that is collecting the TODO list.
text_file_location = rootdir + "/TODO.txt"
print(text_file_location)
# '/Users/chandlerkilpatrick/.julia/dev/SHERPA/TODO.txt'

# Opens and writes the TODO.txt file.
TODO_file = open(text_file_location, 'w')

# All the possible variations to look for.
possible_TODO = ["#TODO", "# TODO:", "# TODO", "TODO:"]


for subdir, dirs, files in os.walk(rootdir):    
    for file in files:
        if True:
            TODO_file.write(f"path {subdir}\n")
            TODO_file.write(f"file {file}\n")
            

# end of all for loops
# Prints the last date modified for convenience. 
TODO_file.write("Last modified: " + str(datetime.datetime.now()))
# Closes the TODO_file
TODO_file.close()
