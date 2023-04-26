class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_cat(self):
        print(f'I am a cat. My name is {self.name}. I am {self.age} years old')

    def make_sound(self):
        print('Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_dog(self):
        print(f'I am a dog. My name is {self.name}. I am {self.age} years old')

    def make_sound(self):
        print('Bark')


cat1 = Cat('Kitty', 2.5)
dog1 = Dog('Fluffy', 4)

print(cat1.name, cat1.age)
print(dog1.name, dog1.age)