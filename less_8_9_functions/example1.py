def get_max_from_list(list_values):
    max_value = list_values[0]
    for element in list_values:
        if element > max_value:
            max_value = element
    return max_value if max_value > 0 else "Max value is less then zero"


a = [-11, -3, -56, -987, -26, -94, -1, 0]
max_a = get_max_from_list(a)
print(max_a)


