d = {"alice": 35, "mark": 25, "April": 19, "jon": 45}
new_d = {}

for name, age in d.items():
    if name[0] != 'a' and name[0] != 'A':
        new_d[name] = age

print(d)
print(new_d)
