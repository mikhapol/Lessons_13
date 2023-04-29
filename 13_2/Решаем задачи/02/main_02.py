from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        age = date.today().year - year
        return cls(name, age)

    def display(self):
        return f'Это {self.name}, ему {self.age} года.'


if __name__ == '__main__':
    person = Person('иван', 19)
    print(person.display())
    person1 = Person.from_birth_year('Николай', 2000)
    print(person1.display())
    person2 = Person.from_birth_year('Иисус', 0)
    print(person2.display())
    print('-------------')
    print(date.today())
    print(date.today().year)
