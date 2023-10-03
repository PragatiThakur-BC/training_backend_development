# example on how break works with for loop
# this example is from python's official documents


"""
points to remember:
 1. range(2,2) / range(n,n) will be empty and for first value of x we cannot the loop will not run
 and else part would be executable
"""
for n in range(2, 10):
    print("check1:", n)
    for x in range(2, n):
        print("check2", x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# Understanding different arguments(positional, keyword, default, arbitrary)
# a function which will show how read arbitrary arguments and keywords
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


