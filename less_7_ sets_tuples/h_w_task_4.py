a = 'a14b6fhkesd'
set_string_a = {'a'}
counter_1 = 0
counter_2 = 0

for char in a:
    counter_1 += 1
    set_string_a.add(char)

for char in set_string_a:
    counter_2 += 1

if counter_1 > counter_2:
    print("This string is not individual characters")
else:
    print("This string has individual characters")

