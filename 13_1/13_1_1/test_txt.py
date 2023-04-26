import pytest
from txt import PositiveNumber


@pytest.fixture
def number5():
    return PositiveNumber(5)


def test_positive_number_init(number5):
    """Когда мы создаем экземпляр класса со значением Х, то get_value вернет нам Х."""
    assert number5.get_value() == 5


def test_positive_number_increment(number5):
    """Когда мы создаем класс со значением Х, затем вызываем increment, то get_value вернет нам Х + 1."""
    number5.increment()
    assert number5.get_value() == 6


def test_positive_number_not_int():
    """Когда мы создаем экземпляр класса с нечисловым значением, вернется ошибка."""
    with pytest.raises(ValueError):
        PositiveNumber('abc')


def test_positive_number_negative():
    """Когда мы создаем экземпляр класса с числовым, но отрицательным значением, вернется ошибка."""
    with pytest.raises(ValueError):
        PositiveNumber(-5)
