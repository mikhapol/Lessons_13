class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    # Геттер для fullname
    @property
    def fullname_p(self):
        """Возвращает полное имя сотрудника. К атрибуту можно обращаться без ()."""
        return f'{self.first} {self.last}'

    # Геттер для email
    @property
    def email(self):
        """Возвращает email сотрудника. К атрибуту можно обращаться без ()."""
        return f'{self.first}.{self.last}@email.com'


emp_1 = Employee('Jon', 'Snow')

print(emp_1.first)
print(emp_1.email)
print('Первый вариант:' + emp_1.fullname())
print('Второй вариант:', emp_1.fullname_p)  # Геттер для fullname
# Выведет:
# Jon
# Jon.Snow@email.com
# Jon Snow
# Jon Snow

# Изменим отдельно атрибут first и снова сделаем принты:
emp_1 = Employee('Jon', 'Snow')
emp_1.first = 'Tim'

print(emp_1.first)
print(emp_1.email)
print('Первый вариант: ', emp_1.fullname())
print('Второй вариант: ' + emp_1.fullname_p)  # Геттер для fullname
# Выведет:
# Tim
# Jon.Snow@email.com
# Tim Snow
# Tim Snow
