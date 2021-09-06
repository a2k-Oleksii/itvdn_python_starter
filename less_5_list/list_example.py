my_list = list('Hello world')
print(my_list)

my_List_2 = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(my_List_2)

my_List_3 = ['H', 55, 'l', True, 'o', False, 'w', 'o', -123, 'l', 'd']
print(my_List_3)

# Cрезы my_list[start:stop:step]
#
print(my_list[0:5])
print(my_List_2[3:3])
print(my_List_3[1:10:3])

my_list.append("new_element")
print(my_list)

my_list.clear()
print(my_list)

my_List_2.extend(my_List_3)
print(my_List_2)

print(my_List_2.index(-123))

removed_element = my_List_3.pop(0)
print(removed_element)
print(my_List_3)

my_List_3.reverse()
print(my_List_3)

my_list_int = [2, 7, 1, 9, 6, 8]
my_list_int.sort()
print(my_list_int)
my_list_int.sort(reverse=True)
print(my_list_int)

my_list_int = [2, 7, 1, 9, 6, 8]
for element in my_list_int:
    print(element)
