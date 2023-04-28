from accessify import private, protected


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    # В классе Employee
    @private
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp = Employee('Jon', 'Snow')
# Обращаемся к атрибутам экземпляра класса

print(emp.first, emp.last)

# Теперь обратиться к set_raise_amt  можно только внутри класса, но не извне:
# Обращение извне
# Employee.set_raise_amt(1.05)
print(dir(emp))
