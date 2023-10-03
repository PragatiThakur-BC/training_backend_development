# example on how brea works with for
# this example is from python's official documents

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

'''
points to remember:
 1. range(2,2) / range(n,n) will be empty and for first value of x we cannot the loop will not run
 and else part would be executable
'''
