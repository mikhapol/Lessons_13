from datetime import date


class Person:
    def __init__(self, name, age):
        self.__name = name.title()
        self.__age = age

    @property  # getter
    def person_name(self):
        return self.__name

    @person_name.setter  # setter
    def person_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            print('Имя некорректно')

    @property  # getter
    def person_age(self):
        return self.__age

    @person_age.setter  # setter
    def person_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print('Возраст некорректный')

    @classmethod
    def from_birth_year(cls, name, year):
        age = date.today().year - year
        return cls(name, age)

    def display(self):
        return f'Это {self.__name}, ему {self.__age} лет.'


if __name__ == '__main__':
    person = Person('Иван', "19")
    print(person.display())
    person1 = Person.from_birth_year('Николай', 2000)
    print(person1.display())
    person2 = Person.from_birth_year('Вася', 1985)
    print(person2.display())
    print('-------------')
    print(date.today())
    print(date.today().year)
    print('-------------')
    print(person.person_name, person.person_age)
    print(person1.person_name, person1.person_age)
    print(person2.person_name, person2.person_age)
    print('-------------')
    person.person_name = '2_Имя_Иисус'  # Имя некорректно
    person.person_age = 0  # Возраст некорректный
    person1.person_name = 123  # Имя некорректно
    print('-------------')
    print(person.person_name, person.person_age)
    print(person1.person_name, person1.person_age)
    print(person2.person_name, person2.person_age)
