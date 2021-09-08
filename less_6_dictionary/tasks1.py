my_list = [1, 1, 1, 3, 3, 3, 2, 2, 4, 5, 6, 7, 7, 7, 7, 7]
value_to_count = 7
count_dict = {value_to_count: 0}

for element in my_list:
    if element == value_to_count:
        count_dict[value_to_count] += 1

print(count_dict)

count_dict2 = {}

for element in my_list:
   if element in count_dict2:
       count_dict2[element] += 1
   else:
       count_dict2[element] = 1

for key, value in count_dict2.items():
    print("key:", key, "count", value)


