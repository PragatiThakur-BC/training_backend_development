# list methods
l1 = ["a", "b", "abc", 1]
# APPEND (adds the item as single unit directly)
l1.append(['ab', 'cd'])
print("Appended items", l1)

# EXTEND (iterates through the data and adds the item)
l1.extend(['ab', 'cd', 12])
print("Extended items", l1)
l1.extend('yz')
print(l1)

# INSERT
# a.insert(len(a), x) is equivalent to a.append(x).
l2 = ['a', 'b', 'ab']
l2.insert(1, 'c')
print(l2)
l2.insert(4, ['abc'])
print(l2)

# REMOVE
l3 = [1, 2, 3, 'a', '', 'ab']
l3.remove(2)
print(l3)
# l3.remove(4) will raise value error as 4 is not present in the list
l3.remove('')
print(l3)

# POP
l4 = [1, 2, 3, 'a', 'b', 'ab']
l4.pop()  # removes the last element
print(l4)
l4.pop(1)  # removes the element at index 1
print(l4)

# del
# del is keyword unlike pop and remove are methods
l5 = [1, 2, 3]
del l5[0]  # deletes the element at 0 index
print(l5)
# to delete complete list use: del list_name

# INDEX
# return the first occurrence of the element
l6 = ['a', 'b', 'c', 1, 2, 'a', 'b', 'ab', 'ac']
print(l6.index('a'))  # first occurrence at 0
print(l6.index('b', 3, len(l6)))  # using index with slicing

# COUNT
l7 = ['a', 'b', 'c', 1, 2, 'a', 'b', 2]
print(l7.count('d'))

# SORT
# you can't sort all lists for example None, 10, 'a' can't be
# sorted as we cannot compare None with other data types
l8 = ['a', 'z', 'y', 'b']
l8.sort()
print(l8)
l9 = ['1', 'a', 'z', '0']
l9.sort()
print(l9)
l10 = ['1', 'a', 'z', '0', 'abcz', 'ab']
l10.sort()
print(l10)

# Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()  # only remove the last ele
print(stack)

# LIST COMPREHENSION
# squares of first 9 numbers in a list
squares = [x**2 for x in range(10)]
print(squares)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
double_vec = [x*2 for x in vec]
print(double_vec)
# filter the list to exclude negative numbers
positive_num = [x for x in vec if x > 0]
print(positive_num)
fresh_fruit = ['banana', 'loganberry', 'passion fruit']
# call a method on each element
length_list = [len(x) for x in fresh_fruit]
print(length_list)
# create a list of 2-tuples like (number, square)
tuple_list = [(x, x**2) for x in range(10)]
print(tuple_list)
# flatten a list using a list comp with two 'for'
vec1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [item for row in vec1 for item in row]
print(flatten_list)

# NESTED LIST COMPREHENSION
# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
# creating matrix/nested list via this method
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)






