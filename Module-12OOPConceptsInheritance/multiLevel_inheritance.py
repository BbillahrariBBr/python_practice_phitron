from math import remainder


class Vehicle:
    def __init__(self,name,license,price) -> None:
        self.name = name
        self.license = license
        self.price = price
        print('Vehicle Init ')
    
    def start(self):
        print(f'{self.name} Started')

class Bus(Vehicle):
    def __init__(self, name, license, price,seat,ticket_price) -> None:
        self.seat = seat
        self.available_seats = seat
        self.ticket_price = ticket_price
        super().__init__(name, license, price)
        print('Bus init')
    
    def sell_ticket(self,customer_name,quantity,amount):
        self.available_seats  -= quantity
        remainder = amount - self.ticket_price * quantity
        if remainder >= 0:
            return Ticket(customer_name)
        return 'No ticket for you'

class AcBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        super().__init__(name, license, price, seat, ticket_price)

class MiniBus(Bus):
    def __init__(self) -> None:
        print('Mini Bus Created')
        super().__init__("Mini Mim", "DkA450", 4580000, 50, 45)

class Ticket:
    def __init__(self,owner) -> None:
        self.owner = owner

mini = MiniBus()
print(mini.name)
print(mini.seat)
print(mini.license)
print(mini.available_seats)