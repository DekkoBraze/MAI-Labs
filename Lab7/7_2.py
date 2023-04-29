def log_errors(func):
    def surrogate(*args):
        try:
           result = func(*args)
           return result
        except ValueError as e:
            print('exception', e)
            file = open('log.txt', mode='a')
            print('exception', e, file=file)
            raise e
    return surrogate


@log_errors
def fun(x, y):
    raise ValueError("В функцию передано некорректное значение")

fun(1, 5)