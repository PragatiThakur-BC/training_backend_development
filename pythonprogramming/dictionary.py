# empty dictionary
d = {}
# adding values
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)
# if we use same key and add value it will rewrite the older on with new value
d['b'] = 10
print(d)
# deleting key - value pair with del keyword
del d['a']
print(d)
# to get list of keys present in the dict
print(list(d))

# creating dictionary using dict()keyword
new_dict = dict([('a', 10), ('b', 11), ('c', 12)])
print(new_dict)

# dictionary comprehensions
multiples = {x: x*2 for x in range(11)}
print(multiples)

# using simple value assignment to string keys
string_dict = dict(a=5, b=7, c=9)
print(string_dict)
