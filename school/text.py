def t(f):

    def wrapper(*args, **kwargs):
        ret = f(*args, **kwargs)
        return ret

    return wrapper


@t
def add(x, y):
    return x + y


print(add(1, 2))
