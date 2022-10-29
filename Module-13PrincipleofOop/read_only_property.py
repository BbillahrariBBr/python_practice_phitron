class Student:
    def __init__(self,name, id,marks) -> None:
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def student_id(self):
        return self.__id
    @property
    def name(self):
        return self._name

    # @name.deleter
    # def name(self):
    #     del self._name

chw = Student('CC',15,55)
print(chw.student_id)
# chw.student_id = 77 
# print(chw.student_id)
print(chw.name)
# del chw.name
print(dir(chw))