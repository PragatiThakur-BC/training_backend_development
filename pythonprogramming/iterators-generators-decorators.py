# ITERATORS
class Iterating:
    """Iterator to loop over data"""
    def __init__(self, data):
        self.data = data
        self.index = -1
        self.length = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length - 1:
            self.index = self.index + 1
            return self.data[self.index]
        else:
            raise StopIteration


obj1 = Iterating('apple')
idata = iter(obj1)
for i in idata:
    print(i)

# Generators
"""
Each time next() is called on it,
the generator resumes where it left off
(it remembers all the data values and which statement was last executed)
"""


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


result = reverse([1, 2, 4, 5, 6])
for i in result:
    print(i)

# Generator expression's
generator_exp = (i * 5 for i in range(10) if i % 2 == 0)

for i in generator_exp:
    print(i)


# Another example with dot product
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x, y in zip(xvec, yvec)))  # generator expression

# DECORATORS


