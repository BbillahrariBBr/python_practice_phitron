""" Manages Bank Account """
class Account():
    accId = 1
    def __init__(self,name,age,nid_num,balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance 

        #update accid
        self.accountId = Account.accId
        Account.accId +=1

    def deposit(self,amount):
        self.balance +=amount 
    
    def withdraw(self,amount):
        self.balance -= amount

acc_1 = Account("Baki",63,600,500)
# acc_2 = Account("billah",65,600,1500)
print("Deposit")
acc_1.deposit(1500)
print(acc_1.balance)
# print(acc_2.accountId)

print("Withdraw")
acc_1.withdraw(500)
print(acc_1.balance)