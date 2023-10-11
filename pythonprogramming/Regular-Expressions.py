# REGULAR EXPRESSIONS
import re
"""
Here are few examples of Regular expression operations.
More can be found out/can be checked at https://www.w3schools.com/python/python_regex.asp
"""
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


# we will use this same function to check result
def check_result(result):
    print(result)
    if result:
        print("Yes found")
    else:
        print("not found")


# using | Either or
txt5 = "It's important to remember to be aware of rampaging grizzly bears."
e = re.findall("to|of", txt5)
print(e)
check_result(e)

"""
SPECIAL SEQUENCE
A special sequence is a '\' followed by one of the characters.
"""
"""
You can create a raw string in Python by prefixing a string literal with r or R. 
Python raw string treats the backslash character '(\)' as a literal character. 
Raw string is useful when a string needs to contain a backslash, 
such as for a regular expression or Windows directory path, 
and you don’t want it to be treated as an escape character.
"""
# \A Returns a match if the specified characters are at the beginning of the string
txt6 = "The rain and Thunder in Seoul"
f = re.findall(r"\AThe", txt6)
check_result(f)

# \b Returns a match where the specified characters are at the beginning or at the end of a word
g = re.findall(r"\brain", txt6)
h = re.findall(r"eoul\b", txt6)
check_result(g)
check_result(h)
