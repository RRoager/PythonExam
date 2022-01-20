from main import Person


class Student(Person):
    pass


tobias = Student("Tobias", "Bojesen", 27)
print(tobias)


print(type(tobias))


print(isinstance(tobias, Person))
