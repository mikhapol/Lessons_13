import datetime


class Employee:  # Класс Работник
    raise_coef = 1.5

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.__pay = pay

    def raise_pay(self):
        self.__pay *= self.raise_coef

    @classmethod
    def from_string(cls, data_string):
        name, surname, pay = data_string.split('/')
        pay = int(pay)

        return cls(name, surname, pay)

    @classmethod
    def set_raise_amount(cls, new_coef):
        cls.raise_coef = new_coef

    @staticmethod
    def is_workday():
        now = datetime.datetime.now()
        # now = datetime.datetime.now().replace(day=22)
        if now.weekday() == 5 or now.weekday() == 6:
            return False
        return True

    @property
    def email(self):
        return f'{self.name.lower()}.{self.surname.lower()}@pochta.ru'

    @property
    def pay(self):
        return self.__pay

    @property  # get
    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'

    @fullname.setter  # set
    def fullname(self, fio_string):
        name, surname = fio_string.split('/')
        self.name = name.title()
        self.surname = surname.title()


if __name__ == '__main__':
    emp1 = Employee('Ivan', 'Ivanov', 60000)

    # TestCase#1 Email
    assert emp1.email == 'ivan.ivanov@pochta.ru'
    # TestCase#6 Email
    emp1.name = 'Semen'
    assert emp1.email == 'semen.ivanov@pochta.ru'

    # TestCase#2 RsisePay
    emp1.raise_pay()

    assert 60000 * Employee.raise_coef == emp1.pay

    assert emp1.pay == 90000

    # TestCase#3 New object
    emp2 = Employee.from_string('Petr/Petrov/70000')
    assert isinstance(emp2, Employee)
    assert emp2.name == 'Petr'
    assert emp2.surname == 'Petrov'
    assert emp2.pay == 70000

    # TestCase#4 Sat raise amount
    Employee.set_raise_amount(2)

    assert Employee.raise_coef == 2
    assert emp1.raise_coef == 2
    assert emp2.raise_coef == 2

    # TestCase#5 Is workday
    assert Employee.is_workday() == True

    # TestCase#7 Get fullname
    assert emp1.fullname == 'Semen Ivanov'
    assert emp2.fullname == 'Petr Petrov'

    # TestCase#8 Set fullname (name, surname)
    emp1.fullname = 'Ivan/Ivanov'
    assert emp1.name == 'Ivan'
    assert emp1.surname == 'Ivanov'
