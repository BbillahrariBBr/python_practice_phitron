# poly = many
#  morph = different
# print(2+8)
class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def make_sound(self):
        print('animal Making Sound')


class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_sound(self):
        print('Meow Meow')

class Dog(Animal):
    def __init__(self, name) -> None:    
        Animal.__init__(self,name)
    def make_sound(self):
        print('bark bark')

class Horse(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('Ney Ney')


don = Cat('Don')
# don.make_sound()

shepard = Dog('German Shepard')
# shepard.make_sound()

don2 = Dog('Asol don')
manik = Horse('Manik Ratan')
# manik.make_sound()

animals = [don,shepard,manik,don2]

for animal in animals:
    animal.make_sound()