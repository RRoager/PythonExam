class Person:
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


class Student(Person):
    def __init__(self, firstname, lastname, age, school):
        super().__init__(firstname, lastname, age)
        self.school = school

    def __str__(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old " \
               f"and studies at {self.school}"


tobias = Student("Tobias", "Bojesen", 27, "KEA")
print(tobias)
print(type(tobias))
print(isinstance(tobias, Person))
