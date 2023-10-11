# Operating System Interface
import os
import sys
import argparse
import re

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
# use terminal with the command python Standard-Library-Tour.py 12 12 12 to get sum of 12 three times!


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

# REGULAR EXPRESSIONS
# Find all lower case characters alphabetically between "a" and "z"
txt = "The day we are practicing python"
x = re.findall("[a-z]", txt)
print(x)

# Find all digit characters remember digit characters means 59 will read 5 and 9 separately
txt1 = "That would be 59 dollar and 3 cents"
y = re.findall("\d", txt1)
print(y)

# Using . dot to find any character except newline
txt2 = "Hi! there\nHi! to you too"
z = re.findall("H..", txt2)
print(z)

# using ^ to find starting word of a string and if we do not use MULTILINE then we will not get any word after newline
a = re.findall("^there", "Lets play\nthere", re.MULTILINE)
print(a)

# using $ to find end of a string word
b = re.findall("around$", "let go and play around")
if b:
    print("Yes, the string ends with 'around'")
else:
    print("No match")

# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
txt3 = "Hello was it his birthday?"
c = re.findall("He.*o", txt3)
print(c)

# Search for a sequence that starts with "he", followed exactly 2 (any) characters, and an "o using dot
txt4 = "Hello, what's up\nHello how was the day\nHelllllo"
d = re.findall("He.{2}o", txt4, re.MULTILINE)
print(d)
