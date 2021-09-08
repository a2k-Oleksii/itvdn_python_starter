my_dict = {'key': 'value', 10: True, 0.2: 'Hello'}
my_dict2 = my_dict

print(my_dict)

print(my_dict['key'])
print(my_dict.get('key2', -1))
print(my_dict2)
print(my_dict2.items())
my_dict2.clear()
print(my_dict2)

d = {1: 10, 3: 30, 4: 40, 7: 70, 5: 50, 9: 90}

print(d.pop(1))
print(d.popitem())

print(d)
d1 = {2: 20, 6: 60}
d.update({3: 'three'})
d.update(d1)

print(d)
print(d.values())
