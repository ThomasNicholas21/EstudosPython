def func1():
    return 'Thomas'


def princ(func):
    return func()


ex = princ(func1)
print(ex)
