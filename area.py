def decor(func):
    def wrapper(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return func(a, b)
        else:
            raise ValueError

    return wrapper


@decor
def area(a, b):
    return a * b
