list_var = [1, 3, 6, -3, 20, 99, 1, 3, 5, 7, 98, -111]
max_num = list_var[0]
count = 0


def max_val():
    global max_num
    max_num = max(list_var)


max_val()
print(max_num)
