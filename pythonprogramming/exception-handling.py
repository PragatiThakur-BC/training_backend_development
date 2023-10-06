# Using try except blocks
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# EXCEPTION CHAINING - error occurs when we get an unhandled exception in except block
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
