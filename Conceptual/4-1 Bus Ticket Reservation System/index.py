


class User:
    def __init__(self,username, password) -> None:
        self.username = username
        self.password = password
    

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]

# class PhitronCompany: # bus install
#     total_bus = 5
#     total_bus_lst = [] # dummy db
#     def install(self):
#         bus_no = int(input("Enter Bus no: "))
#         for w in self.total_bus_lst: # checking kono bus already installed kina
#             if bus_no == w['coach']

a = Bus(10,'Naim','12Pm', '12.30pm', 'Dhaka', 'Khulna')
# not code today
