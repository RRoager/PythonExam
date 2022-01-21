from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()


with open_file('text.txt', 'w') as file:
    file.write('Hej med dig igen')

f = open('text.txt', 'w')
f.write('Hej med dig')
f.close()

with open('text.txt', 'w') as f:
    f.write('Hej med dig igen igen')

with open('text.txt', 'r') as f:
    print(f.read())


