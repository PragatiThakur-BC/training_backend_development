fhand = open('filehandlingexample.txt')
"""
this gives handle of file(Kind of wrapper around file)within which we can interact 
to read, write, update any file operations.
"""
print(fhand)
# Counting number of lines in file
count = 0
for line in fhand:
    count = count + 1
print("Num of lines in file : ", count)
"""
We can put an if statement in
our for loop to only print lines
that meet some criteria
"""
for line in fhand:
    line = line.rstrip() # reason to do this when we print the print gives new line after each line to print
    if line.startswith('R'):
        print(line)
"""
Error handling while reading/opening file due to incorrect file name
"""
fname = input("Enter file name : ")
try:
    fhandle = open(fname)
except:
    print("The file {0} doesn't exists/cannot be opened".format(fname))
    quit()
# quit() stops execution if we get error for example here if file doesn't exist.
# if file exists count the number of lines
count = 0
for line in fhandle:
    count = count + 1
print("Num of lines in file {0} are {1} : ".format(fname, count))