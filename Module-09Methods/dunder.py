# dunder
# magic
# special methods
class Person:
    def __init__(self, name, age, money,height =65) -> None:
        self.name = name
        self.age = age
        self.money = money
        self.height = height
    
    def __call__(self):
        print( f'this is {self.name} with age {self.age} and have {self.money}')
    
    def __eq__(self,other):
        return self.age == other.age
    
    def __len__(self):
        return self.height
    
    def __repr__(self):
        return f'Nmae: {self.name} age: {self.age}'
    def __add__(self,other):
        return self.money+other.money

alim = Person('Alim',15,560)
dalim = Person('Dalim',16,750)
print(alim+dalim)
x = 5
alim()

print(alim == dalim)

friends = [45,65,98,12,32]
print(len(alim))
print(dalim)
