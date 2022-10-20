# dunder
# magic
# special methods
class Person:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self.age = age
        self.money = money
    def __add__(self,other):
        return self.money+other.money

alim = Person('Alim',15,560)
dalim = Person('Dalim',16,750)
print(alim+dalim)
x = 5
    
