variable = 1


def change_glob_var(new_variable):
    global variable
    variable = new_variable


print("Old variable -", variable)
change_glob_var('New variable')
print("New variable -", variable)
