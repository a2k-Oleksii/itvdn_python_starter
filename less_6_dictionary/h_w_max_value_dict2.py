d = {'a': 3, 'b': 'hello', 'c': 4, 'd': -3}
dict_key = ''
dict_value = d.get('a')

for key, value in d.items():
    if type(value) == int:
        if value > int(dict_value):
            dict_value = value
            dict_key = key

print(d.get(dict_key))
