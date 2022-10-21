class Shopping:
    mall= 'Jamuna Future Park'
    hours = []
    def __init__(self,customer):
        self.customer = customer
        self.items = []
        self.total = 0
    @classmethod
    def opennig_hour(csl,day):
        return cls.mall


    @staticmethod
    def multiply(x,y):
        return x,y

    def add_to_total(self,amount,):
        self.total += amount

    def add_to_cart(self,item,price,quantity):
        item_total  = price* quantity
        self.add_to_total += item_total
        self.items.append(item)

    def checkout(self):
        pass

res = Shopping.multiply(45,5)
print(res)
my_shopping = Shopping('Sakib')
my_shopping.add_to_total(450)
my_shopping.add_to_total(450)
print(my_shopping.total)
res2 = my_shopping.multiply(15,4)
print
# res2 = Shopping.add_to_total()