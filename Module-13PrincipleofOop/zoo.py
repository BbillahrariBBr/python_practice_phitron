from abc import ABC, abstractmethod
# abstract base class


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    def name(self):
        pass
    @abstractmethod
    def move(self):
        print('Moving on the zoo')

class Monkey(Animal):
    def sing(self):
        print('Monkey is singing')
    def eat(self):
        print('Eating banann')
    def move(self):
        print('Hanging on the branches of the trees')
        super().move()


layka = Monkey()

print(layka)
layka.eat()
layka.move()