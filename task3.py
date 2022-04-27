def typ_logger(func):
    def wrapper(*args):
        calc_args = func(*args)
        print(f'{func.__name__}', end='')
        if len(args) == 1:
            print(f'{args[0]}: {type(args[0])}')
        else:
            for el in args:
                print(f'{el}: {type(el)}')
        return calc_args
    return wrapper

@typ_logger
def calc_cube(x, *args):
    return x ** 3

print(calc_cube(8, 2))
