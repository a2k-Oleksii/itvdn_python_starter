x = [3, 4, 2, 1, 7, 0, -3, 13, 28, 100, -78, 10]
max_element = x[0]

for element in x:
    if element > max_element:
        max_element = element

print(max_element)
