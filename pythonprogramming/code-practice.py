"""
Problem 1: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
"""


def multiplesof3and5(num):
    total = 0
    for i in range(0, num):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
    return total


print(multiplesof3and5(10))  # for we have 3, 5, 6, 9 as numbers less than 10 divisible by 3 and 5 sum = 23
"""
finding total multiples of two number's less than some value like: 100/1000/2000 in O(1) time instead of O(N)
here : total multiples of 3 and 5 below 100/10
"""


def no_of_multiple(num):
    return num // 3 + num // 5 - num // 15


print(no_of_multiple(10))
"""

"""
