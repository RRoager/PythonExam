def generate_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


generator_fibonacci_list = []


seq = generate_fibonacci()
print(seq)
generator_fibonacci_list.append(next(seq))
generator_fibonacci_list.append(next(seq))
generator_fibonacci_list.append(next(seq))
generator_fibonacci_list.append(next(seq))
generator_fibonacci_list.append(next(seq))
print(generator_fibonacci_list)


fibonacci_list = []


def iterate_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        n1, n2 = n2, n1 + n2
        fibonacci_list.append(n1)


# iterate_fibonacci()
# print(fibonacci_list)


generator = (i for i in range(100000000))

generator_expr_list = []

print(generator)
generator_expr_list.append(next(generator))
generator_expr_list.append(next(generator))
generator_expr_list.append(next(generator))
generator_expr_list.append(next(generator))
generator_expr_list.append(next(generator))
print(generator_expr_list)


