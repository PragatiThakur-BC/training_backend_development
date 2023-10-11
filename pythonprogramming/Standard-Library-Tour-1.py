# Operating System Interface
import os
import sys
import argparse
# gets us the current directory we are working from
print(os.getcwd())
# dir(os)  returns a list of all module functions
for i in dir(os):
    print(i)
# help(os) return documentation related to the library which was written as docstring
help(os)

# COMMAND LINE ARGUMENTS
# USING SYS.ARGV MODULE
"""
len(sys.argv) provides the number of command line arguments
sys.argv[0] is the name of the current Python script.
"""
n = len(sys.argv)
print("Total arguments passed:", n)

print("\nName of Python script:", sys.argv[0])
# Accessing the arguments passed
print("\nArguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")
summation = 0
for i in range(1, n):
    summation = summation + int(sys.argv[i])

print("\nsum of numbers : ", summation)
# use terminal with the command python Standard-Library-Tour-1.py 12 12 12 to get sum of 12 three times!


# USING ARGPARSE
# Adding message
msg = "Adding description"
# initializing parser
parser = argparse.ArgumentParser(description=msg)
# Positional Argument
parser.add_argument("square", help="display square of a number", type=int)
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
answer = args.square ** 2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)




