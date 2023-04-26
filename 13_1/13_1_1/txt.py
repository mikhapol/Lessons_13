class PositiveNumber:
    """Класс для хранения неотрицательного целого числа."""

    def __init__(self, value):
        """Экземпляр класса инициализируется только целым неотрицательным числом."""
        if not isinstance(value, int):
            raise ValueError('Значение должно быть числом.')
        elif value <= 0:
            raise ValueError('Число должно быть неотрицательным.')
        self.value = value

    def increment(self):
        """Метод для увеличения значения числа на единицу."""
        self.value += 1

    def get_value(self):
        """Метод для получения значения числа."""
        return self.value
