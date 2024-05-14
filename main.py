"""
1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
(например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
переопределите методы, если требуется (например, различный звук для `make_sound()`).
3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
 которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
 о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые
 могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
 `heal_animal()` для `Veterinarian`).
 Дополнительно:
 Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение
 информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было
 "постоянное состояние" между запусками программы.
"""
import sys
import pickle

class Animal:
    def __init__(self, name, age, voice, eat):
        self.name = name
        self.age = age
        self.voice = voice
        self.eat = eat

    def make_sound(self):
        print(f"{self.name} говорит {self.voice}")

    def eat_food(self):
        print(f"{self.name} ест {self.eat}")

class Bird(Animal):
    def __init__(self, name, age, voice, eat):
        super().__init__(name, age, voice, eat)

class Mammal(Animal):
    def __init__(self, name, age, voice, eat, breed):
        super().__init__(name, age, voice, eat)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} породы {self.breed} говорит {self.voice}")

class Reptile(Animal):
    def __init__(self, name, age, voice, eat):
        super().__init__(name, age, voice, eat)

class ZooKeeper:
    def __init__(self, name, animals=None):
        if animals is None:
            animals = []
        self.name = name
        self.animals = animals

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")
        animal.eat_food()

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Добавлен сотрудник: {staff_member.name}")

    def list_animals(self):
        print("Список животных:")
        for animal in self.animals:
            print(f"{animal.name}, возраст: {animal.age}, звук: {animal.voice}, еда: {animal.eat}")

    def list_staff(self):
        print("Список сотрудников:")
        for staff_member in self.staff:
            print(staff_member.name)

# Пример использования
zoo = Zoo()

# Добавление животных
bird = Bird("Попугай", 2, "Чирик", "Семена")
mammal = Mammal("Собака", 5, "Гав", "Корм", "Лабрадор")
reptile = Reptile("Змея", 3, "Шшш", "Мыши")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Добавление сотрудников
zookeeper = ZooKeeper("Алексей")
veterinarian = Veterinarian("Мария")

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

# Вывод списка животных и сотрудников
zoo.list_animals()
zoo.list_staff()

# Демонстрация работы сотрудников
zookeeper.feed_animal(mammal)
veterinarian.heal_animal(bird)
