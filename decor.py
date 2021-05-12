from datetime import datetime


def decorator(func):
    def wrapper(*args):
        a = func(*args)
        return a * 2

    return wrapper


@decorator
def sum_args(*args):
    return sum(args)


print(sum_args(12, 23, 4))
