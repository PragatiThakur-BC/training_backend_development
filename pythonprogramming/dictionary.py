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

# looping techniques
# using items:
value_dict = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for k, v in value_dict.items():
    print(k + " for " + v)

# looping via enumerate to get indexes and corresponding value at the same time
for i, v in enumerate(['user-id', 'user_name', 'user_contact']):
    print(i, v)

# looping two dictionaries at the same time
user_key = {'id', 'name', 'role'}
user_info = {'a-1', 'Bella', 'SE'}
print("table data")
for k, v in sorted(zip(user_key, user_info)):
    print("key {0} : value {1}" .format(k, v))

# looping over sequence to print in reverse order
for i in reversed(range(0, 11, 2)):
    print(i)

# looping on sorted manner
dict_unsort = {'b': 'berry', 'c': 'cherry', 'a': 'apple'}
for i, v in sorted(dict_unsort.items()):
    print(i, v)
