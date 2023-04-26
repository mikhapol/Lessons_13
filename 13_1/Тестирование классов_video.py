"""
Описать метод для класса Employee, который позволяет
индексировать зарплату сотруднику по заданному коэффициенту
"""


class Employee:
    raise_coef = 1.5

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.email = f'{self.name.lower()}.{self.surname.lower()}@pochta.ru'
        self.pay = pay

    def raise_pay(self):
        self.pay *= self.raise_coef


if __name__ == '__main__':
    emp1 = Employee('Ivan', 'Ivanov', 60000)

    # TestCase#1 Email
    assert emp1.email == 'ivan.ivanov@pochta.ru'

    # TestCase#2 RsisePay
    emp1.raise_pay()

    assert 60000 * Employee.raise_coef == emp1.pay

    assert emp1.pay == 90000
