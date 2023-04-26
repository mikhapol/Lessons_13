# Пошаговая инструкция создания класса
# 1 - Определите название класса и его суть.
# 2 - Определите поля (свойства) класса.
# 3 - Определите конструктор класса.
# 4 - Определите методы класса.
# 5 - Определите атрибуты класса, если необходимо.


class Employee:
    """Класс для представления сотрудника."""

    # Переменная на уровне класса, доступна из любых экземпляров
    raise_amount = 1.05

    # Переменная на уровне класса для подсчета количества сотрудников
    nummer_of_employees = 0

    def __init__(self, name, surname, pay):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.surname = surname
        self.email = f'{self.name}.{self.surname}@ru.ru'
        self.pay = pay

        Employee.nummer_of_employees += 1

    def fullname(self):
        """Метод, который возвращает полное имя сотрудника."""
        return f'{self.name} {self.surname}'  # self позволяет использовать данные конкретного экземпляра

    # Внутри класса Employee
    def apply_raise(self):
        """Метод для индексации заработной платы."""
        self.pay = int(self.pay * self.raise_amount)


# Создаем 1-й экземпляр и передаем параметры для инициализации
emp_1 = Employee('Ivan', 'Ivanov', 50000)
# Создаем 2-й экземпляр и передаем параметры для инициализации
emp_2 = Employee('Pert', 'Petrov', 60000)

# print(emp_1)
print(emp_1.name)
print(emp_1.surname)
print(emp_1.pay)
print(emp_1.email)
print(emp_2.email)

# Вызываем метод fullname экземпляра emp_1 и выводим результат в консоль
print(emp_1.fullname())
# Вызываем метод fullname экземпляра emp_2 и выводим результат в консоль
print(emp_2.fullname())

# Выводим текущую зарплату
print(emp_1.pay)
# Вызываем метод для повышения з/п
emp_1.apply_raise()
# Выводим новую з/п
print(emp_1.pay)

# Выводим количество сотрудников
print(Employee.nummer_of_employees)