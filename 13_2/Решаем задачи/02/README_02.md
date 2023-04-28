Задача 2

Создайте класс 
Person
, содержащий два атрибута: имя и возраст.

Создайте метод класса 
fromBirthYear
 с альтернативным способом создания экземпляра класса 
Person
 — когда указан год рождения.

person = Person('Иван', 19)
person.display()

person1 = Person.fromBirthYear('Николай',  2000)
person1.display()

# вывод
Иван. Возраст: 19
Николай. Возраст: 23

Получить текущий год можно так:

from datetime import date

print(date.today().year)