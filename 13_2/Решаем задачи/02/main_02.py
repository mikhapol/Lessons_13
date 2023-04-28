from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year_of_birth):
        age = date.today().year - year_of_birth
        return cls(name, age)

    def display(self):
        return f'Это {self.name}, ему {self.age} года.'


person = Person('Иван', 19)
print(person.display())
person1 = Person.fromBirthYear('Николай', 2000)
print(person1.display())
person2 = Person.fromBirthYear('Иисус', 0)
print(person2.display())
print('-------------')
print(date.today())
print(date.today().year)
