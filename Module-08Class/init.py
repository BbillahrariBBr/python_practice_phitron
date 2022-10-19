
class Phone:
    manufactured = 'China'
    def __init__(self,brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    def send_sms(self,number,txt):
        sms = f'sending: {txt} to {number}'
        return sms

my_phone = Phone('Oppo',13000,'blue')
print(my_phone.brand, my_phone.manufactured)
