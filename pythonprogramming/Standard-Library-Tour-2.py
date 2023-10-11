# Mathematics module- math, random, statistics
import math
import random
import statistics
print("Factorial of '5' using inbuilt func:", math.factorial(5))
print("tan(45): ", math.tan(math.pi/4))
print("log value of 128 with 2:", math.log2(128))
print("log value of 128 with 3:", math.log(128, 3))

# The random module provides tools for making random selections
print("random choice from a to f : ", random.choice(["a", "b", "c", "d", "e", "f"]))
print("random sample with 10 units and replacement: ", random.sample(range(1000), 10))
print("random float number between 0 and 1 :", random.random())
print("random integer from n1 to n2 :", random.randint(10, 25))

# statistics module can do maximum statistical operations
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
print("MEAN: ", statistics.mean(list1))
print("MEDIAN: ", statistics.median(list1))
print("MODE:", statistics.mode(list1))
print("Quantile:", statistics.quantiles(list1))


