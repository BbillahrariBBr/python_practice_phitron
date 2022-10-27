""" All about Mankind inheritance """


class Human():
    def __init__(self,gender,height,weight):
        self.gender=gender
        self.height = height
        self.weight = weight

class Police(Human):
    def __init__(self,cases, nationality, gender, height, weight):
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality

class CSE(Human):
    def __init__(self,love_to_Code,has_gf, gender, height, weight):
        super().__init__(gender, height, weight)
        self.love_to_Code = love_to_Code
        self.has_gf = has_gf

# police = Police(True, "Bangladeshi","male",84,64)
# print(police.height)

cse = CSE(True,False,"male",847,64)
cse2 = CSE(love_to_Code=False,gender="female",has_gf=False,height=45, weight=65)
print(cse.has_gf)