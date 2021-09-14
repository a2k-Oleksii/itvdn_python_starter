def x():
    a = 10


try:
    print(int('abc'))
except ValueError as error:
    print(error)
except NameError as error:
    print(error)
