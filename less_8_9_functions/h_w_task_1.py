def some_function(a_number, b_number):
    if type(a_number) == int and type(b_number) == int:
        if a_number+b_number >= 0:
            print(0)
        else:
            print(-1)
    else:
        print(1)


some_function(0, 0)
