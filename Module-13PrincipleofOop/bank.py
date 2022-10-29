from mimetypes import init


class Account:
    def __init__(self,holder,initaial_balance) -> None:
        self.holder = holder # public attribute
        self._account_number = 165
        self.__balance = initaial_balance # __balance is a private attribute
    def deposit(self,amount):
        print(f'adding {amount} to your account')
        self.__balance += amount
    
    def withdraw(self,amount):
        print(f'Withdrawing {amount} from your account')
        self.__balance-= amount


class StudentAccount(Account):
    def __init__(self,holder,initaial_balance,school):
        self.school = school
        super().__init__(holder,initaial_balance)
    
    def get_balance(self):
        return 


rafsan = StudentAccount('Rafsan',40000,"IUB")
# print(rafsan.__balance)
print(rafsan.holder)
rafsan.deposit(20000)
rafsan.deposit(35000)
rafsan.deposit(15000)
# rafsan.__balance = 0
print(rafsan._account_number)