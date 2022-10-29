""" laptop phone watch tablet """
# base class will have only the common attributes and methods
class Device:
    def __init__(self,brand,price,color) -> None:
        self.brand = brand
        self.price = price
        self.color = color
    
    def re_sale(self):
        print('Ready to sell again')


class Laptop(Device):
    def __init__(self,brand,price,color,disc_size) -> None:
        super().__init__(brand,price,color)
        self.spec = disc_size
    def run(self):
        print('Running The laptop')
    def purchase(self,money,discount):
        if money < (self.price  - self.price * discount /100):
            return 'No laptop for you'
        else:
            print('This device for you')
            return money-self.price
    def __repr__(self) -> str:
        return f'laptop {self.brand}: {self.price} - {self.color}'

class Phone:
    def __init__(self,brand, price,color,camera, sim_num) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_num = sim_num
    
    def is_dual_sim(self):
        return self.sim_num > 1
    
    def purchase(self,money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print('This device for you')
            return money-self.price
    
    def __repr__(self) -> str:
        return f'Phone {self.brand}: {self.price} - {self.color}'
    

class Watch:
    def __init__(self,brand,price,color,watch_type) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type
    def is_digital(self):
        return self.watch_type == 'digital'
    
    def purchase(self,money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print('This device for you')
            return money-self.price

class Manager:
    def __init__(self,name,salary,experience,designation) -> None:
        pass

    def withdraw_salary(self):
        pass

    def day_total_sales(self):
        pass

    def handle_customer_complain(self):
        pass

class SalesPesrson:
    def __init__(self,name,salary,experience,designation,commission) -> None:
        pass

    def handle_customer(self):
        pass

    def withdraw_salary(self):
        pass


lenovo = Laptop('Lenoovo',42000,'black','500gb')
hp = Laptop('Hp',458000,'silver','500gb')
oppo = Phone("Oppo",25000, "Black","5mp",2)
samsung = Phone("samsung",45000, "Black","12mp",2)
print(hp)
hp.re_sale()