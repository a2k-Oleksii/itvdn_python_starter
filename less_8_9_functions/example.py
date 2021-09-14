x = [1, 2, 3, 4, 5]


def make_smth(function):
    for element in x:
        print(function(element))


make_smth(lambda a: a + a)
print('---------------------------------------')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))
