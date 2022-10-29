# public
# protected
# private
class Account:
    def __init__(self,holder) -> None:
        self._account_holder = holder

class StudentAccount(Account):
    def __init__(self,holder,balance,school) -> None:
        self.__balance = balance

    def withdraw(self,amount):
        if amount > self.__balance:
            return 'No money for You'
        self.__balance -=amount
        return amount
    
    def deposit(self,amount):
        if amount < 0:
            return 'negative amount can not be added'
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

nas = StudentAccount('nas daily', 12000, 'Nas Academy')
# print(nas.get_balance())

print(dir(nas)) # private variable dekhar jjnno
print(nas._StudentAccount__balance) # private variable print 
