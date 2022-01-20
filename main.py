class Person:
    def __init__(self, firstname, lastname, age):
        self._firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self._firstname} {self.lastname} is {self.age} years old"

    def __repr__(self):
        return f"Person({self._firstname}, {self.lastname}, {self.age})"

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value


rasmus = Person("Rasmus", "Roager", 34)
print(rasmus)
print(repr(rasmus))



print(rasmus.firstname)
rasmus.firstname = "Bent"
print(rasmus.firstname)


class Student(Person):
    pass


tobias = Student("Tobias", "Bojesen", 27)
print(tobias)
print(type(tobias))

print(isinstance(tobias, Person))

my_set = {3, 4, 1, 2}

my_set.remove(3)
print(my_set)


generator = (i for i in range(10))

print(generator)


def generate_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


seq = generate_fibonacci()
print(seq)
f1 = next(seq)
print(f1)
f2 = next(seq)
print(f2)
f3 = next(seq)
print(f3)
f4 = next(seq)
print(f4)
f5 = next(seq)
print(f5)

fibonacci_list = []

def iterate_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        n1, n2 = n2, n1 + n2
        fibonacci_list.append(n1)


#iterate_fibonacci()
#print(fibonacci_list)

#f = open('text.txt', 'w')
#f.write('hej med dig igen')
#f.close()

#with open('text.txt', 'w') as f:
#    f.write('Hej med dig igen igen')


with open('text.txt', 'r') as f:
    print(f.read())


from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()


with open_file('text.txt', 'r') as f:
    print(f.read())


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



