from abc import ABC, abstractmethod
# abstract base class


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @property
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def move(self):
        print('Moving on the zoo')

class Monkey(Animal):
    def __init__(self) -> None:
        self.__name = 'Monkey'
    def sing(self):
        print('Monkey is singing')
    def eat(self):
        print('Eating banann')
    def move(self):
        print('Hanging on the branches of the trees')
        super().move()
    @property    
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value


layka = Monkey()

print(layka)
layka.eat()
layka.move()
layka.name = "Donkey"
print(layka.name)

