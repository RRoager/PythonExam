def debugger(func):
    def wrapper(*args):
        print(f'DEBUG:  func: {func.__name__}')
        print(f'DEBUG:  args: {args}')
        result = func(*args)
        print(f'RESULT: {result}')
        return result
    return wrapper


@debugger
def add(a, b):
    return a + b


add(5, 5)

