# class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old"

    def __repr__(self):
        return f"Person({self.firstname}, {self.lastname}, {self.age})"

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