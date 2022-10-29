# print(max(12,45,87,98,45,63,458,-8))
# print(max([12,45,87,98,45,63,458,-8]))
# print(max('A','P','K','C'))


def add(num1,num2):
    return num1+num2

print(add(12,13))
# print(add(12,13,50))

# op overlaoding
class Account:
    def __init__(self,holder,balance) -> None:
        self.holder = holder
        self.__balance = balance
    
    def __add__(self,other):
        return self.__balance + other.__balance
    def __eq__(self, __o: object) -> bool:
        return self.__balance == __o.__balance
my_acc = Account('Shakib',6000)
her_acc = Account('shishir',90000)
res = my_acc+her_acc
print(res)