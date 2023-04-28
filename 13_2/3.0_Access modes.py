# 3. Режимы доступа

class EmployeePublic:
    def __init__(self, first, last):
        """
        Режим доступа public
        """
        self.first = first
        self.last = last


emp = EmployeePublic('Employee1', 'Public')
# Обращаемся к атрибутам экземпляра класса
print(emp.first, emp.last)


class EmployeeProtected:
    def __init__(self, first, last):
        """
        Режим доступа protected
        """
        self._first = first
        self._last = last


emp = EmployeeProtected('Employee2', 'Protected')
# Обращаемся к атрибутам экземпляра класса
print(emp._first, emp._last)


class EmployeePrivate:
    def __init__(self, first, last):
        """
        Режим доступа private
        """
        self.__first = first
        self.__last = last

    # В классе EmployeePrivate
    def fullname(self):
        return f'{self.__first} {self.__last}'


emp = EmployeePrivate('Employee3', 'Private')

# Oбращаемся к атрибутам экземпляра класса
print(EmployeePrivate.fullname(emp))

# print(emp.__first, emp.__last) # Будет ошибка

# print(dir(emp))
# ['_EmployeePrivate__first', '_EmployeePrivate__last', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'fullname']

print(emp._EmployeePrivate__first, emp._EmployeePrivate__last)