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

    def eat(self):
        print(self.eat)

class Bird(Animal):
    def __init__(self, name, age, voice, eat):
        super().__init__(name, age, voice, eat)
    #     self.voice = voice
    #
    def make_sound(self):
        print(self.voice)

class Mammal(Animal):
    def __init__(self, name, age, voice, eat, breed):
        super().__init__(name, age, voice, eat)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} породы {self.breed} говорит {self.voice}")

class Reptile(Animal):
    def __init__(self, name, age, voice, eat):
        super().__init__(name, age, voice, eat)
        self.voice = voice

    def make_sound(self):
        print(self.voice)

class ZooKeeper():
    def __init__(self, name, animals):
        self.name = name
        self.animals = animals

    def feed_animal(self):
        pass

class Veterinarian():
    def __init__(self):
        pass

    def heal_animal(self):
        pass

class Zoo():
    def __init__(self):
        pass

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Создание объектов класса Bird
crow = Bird("crow", 5,"кар", "")
duck = Bird("duck", 3,"кря", "планктон")

# Создание объектов класса Mammal
dog = Mammal("собака", 7,"гав", "мясо", "овчарка")
cat = Mammal("кошка", 1,"мяу", "сметана", "сфинкс")
# Тестирование функции с созданными объектами
animals_list = [crow, duck, dog, cat]
# animal_sound(animals_list)

def exit_zoo():
    pass

def main():
    # try:
    #     with open('animals_list.pkl', 'rb') as file:
    #         animals_list = pickle.load(file)
    # except FileNotFoundError:
    #     animals_list = []

    animal_sound(animals_list)
    print("\nМеню программы управления зоопарком")
    print("0 - выход из программы")
    print("1 - добавление нового животного в список зоопарка")
    print("2 - добавление нового сотрудника в штат зоопарка")
    print("3 - просмотр списка животных зоопарка")
    print("4 - просмотр списка сотрудников зоопарка")

    while True:
        choice = input('\n'"Выберите пункт меню (0-4): ")
        if choice == '0':
            with open('animals_list.pkl', 'wb') as file:
                pickle.dump(animals_list, file)
            exit_program()
        elif choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            for animal in animals_list:
                print(f"Name: {animal.name}, Age: {animal.age}, Voice: {animal.voice}, Eat: {animal.eat}")
        elif choice == '4':
            pass
        else:
            print("Неверный ввод. Пожалуйста, выберите от 1 до 4.")

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

if __name__ == "__main__":
    main()
