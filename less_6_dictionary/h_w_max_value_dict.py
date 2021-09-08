d = {'a': 3, 'b': 0, 'c': 4, 'd': -3}
dict_key = ''
dict_value = d.get('a')

for key, value in d.items():
    if value > dict_value:
        dict_value = value
        dict_key = key
print(d.get(dict_key))
