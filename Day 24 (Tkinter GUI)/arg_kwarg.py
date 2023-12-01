# args vs Kwargs


def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


add(1, 2, 3, 4, 5)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

