# LAMBDA , MAP(), REDUCE(), FILTER()
from functools import reduce
"""
from functools import reduce
Starting with lambda function and continuing further
with how to use lambda with other functional programming
methods!
"""
str1 = "Never underestimate the willingness of the greedy to throw you under the bus"
upper_case = lambda string: string.upper()
print(upper_case(str1))

# LAMBDA FUNCTION USAGE:
# Condition checking using the lambda function
"""
we are formatting the number if the number is integer then format it as scientific number
else if number is float then we are formatting it as to see it comma separated with two decimal values.
"""
format_num = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.3f}"
print("Integer num 1000: ", format_num(1000))
print("Float num 9999.88898912: ", format_num(9999.88898912))


# Difference between lambda and def defined function
def square(num):
    return num * num


lambda_square = lambda num: num * num
print("using def keyword: ", square(5))
print("using lambda function: ", lambda_square(5))

# Lambda with List Comprehension
# we are calling the function object having default argument using value()
multiple_list = [lambda arg=x: arg * 10 for x in range(1, 6)]
for value in multiple_list:
    print(value())

# Lambda with if-else
maximum = lambda num1, num2: num1 if(num1 > num2) else num2
print(maximum(22, 33))

# Lambda with Multiple Statements
"""
Lambda functions don't allow multiple statements however we can
create two lambda functions and call the other lambda funtion as parameter
to the another function
"""
# example for sorting list of lists and to get list of second-largest number in each list
list1 = [[3, 2, 1], [6, 5, 7], [8, 9, 10]]
# lamda function to sort each list in list1
sorted_list = lambda x: (sorted(i) for i in x)
# lambda function which takes two arguments 1.List 2.Function
secondLargest = lambda x, f: [y[len(y)-2] for y in f(x)]
result = secondLargest(list1, sorted_list)
print(result)

# USING LAMBDA WITH FILTER()
list2 = [2, 3, 4, 5, 7, 8, 10, 12]
filtered_list = list(filter(lambda x: (x % 2 == 0), list2))
print(filtered_list)

# USING LAMBDA WITH MAP()
list3 = [2, 3, 4, 5, 6, 7, 8, 10]
final_list = list(map(lambda x: x*2, list3))
print(final_list)

# USING LAMBDA WITH REDUCE()
"""
reduce() works differently than map() and filter().
It does not return a new list based on the function and iterable we've passed.
Instead, it returns a single value.
Also, in Python 3 reduce() isn't a built-in function anymore,
and it can be found in the functools module.
"""
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_value = reduce((lambda x, y: x + y), list4)
print(sum_value)


