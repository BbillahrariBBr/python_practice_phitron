class Employee:
    def __init__(self,name,id, salary, position,experience) -> None:
         self. name = name
         self.id = id
         self.salary = salary
         self.position = position


class Developer(Employee):
    def __init__(self, name, id, salary, position,tech,focus) -> None:
        self.tech = tech
        self.area_of_work = focus
        super().__init__(name, id, salary, position)

class Testing(Employee):
    pass

class Sales(Employee):
    pass


class TechLead(Employee):
    pass