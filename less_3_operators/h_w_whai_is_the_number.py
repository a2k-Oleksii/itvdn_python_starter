number = -0


def counting_number_rows(num):
    if num < 10:
        print("has one symbol")
    elif num < 100:
        print("has two symbol")
    elif num < 1000:
        print("has three symbol")
    else:
        print("has fore and more symbol")


if number == 0:
    print("This is special number 0")
elif number > 0:
    print("This is a positive number ", end="")
    counting_number_rows(number)
else:
    print("This is a negative number ", end="")
    number = -number
    counting_number_rows(number)
