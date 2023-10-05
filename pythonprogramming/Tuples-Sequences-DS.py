# Accessing elements of list in tuple
v = ([1, 2, 3], [3, 2, 1])
# accessing single elements of list
print(v[0][1])
# accessing multiple elements of list via slicing
print(v[1][0:3])

# creating single ele tuple
empty = ()
singleton = 'hello',
print(len(empty))
print(singleton)
# sequence unpacking
tup = 12345, 54321, 'hello!'
x, y, z = tup
print(x, y, z)

# methods
tup1 = 1, 2, 3, 4, 5, 6, 7, 7, 7, 9, 1, 23, 3
print(tup1.count(3))
print(tup1.index(7))
