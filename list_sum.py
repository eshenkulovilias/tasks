a = [13, 'hello', (3, 5), [8, ], 903, 5.9]


def func(lst):
    summ = 0
    for i in lst:
        try:
            summ += i
        except TypeError:
            continue

    return summ


print(func(a))
