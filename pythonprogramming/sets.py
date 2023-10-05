# set creation
set1 = {1, 2, 23, 4, 3, 5, 1, 2, 3, 4}
print(set1)  # order's the number in sequence, and removes duplicates
# membership testing
print(1 in set1)
print(10 in set1)

# set operations on two different sets
a = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
b = {'d', 'e', 'f', 'g', 'h', 'i', 'j'}
# letters in set-a but not in b
print(a-b)
# letters in a or b or both
print(a | b)
# letters in both a and b
print(a & b)
# letters in a or b but not in both
print(a ^ b)

# update set values
new_set = {1, 2, 3, 4}
new_set.update(('a', 'b'))
print(new_set)
# removing values
new_set.remove(2)
print(new_set)
# discard - does not raise error even if an ele is not present
print(new_set.discard(10))
# pop - pops random element from set
print(new_set.pop())
print(new_set.pop())
# clear - removes all elements of set
print(new_set)
print(new_set.clear())
print(new_set)

# frozen sets - This has all the properties of a set, except that it is immutable
"""
The frozenset datatype has all the methods of a set
(such as difference(), symmetric_difference, and union) but because it is immutable,
it doesn't have methods to add/remove elements.
"""
f_set1 = frozenset(('a', 'b', 'c'))
f_Set2 = frozenset(('d', 'e'))
print(f_set1.issubset(f_Set2))

# we can use frozen-sets as dictionaries
d = {f_set1: 'hello', f_Set2: 'world'}
print(d)
