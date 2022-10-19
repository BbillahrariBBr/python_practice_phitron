def add(a,b):
    sum = a+b
    print(sum)
def deduct(x,y):
    res = x-y
    return res

class Phone:
    color = 'black'
    features = ['camera', 'water proof','can be used as a hammer']

    def call(self):
        print('ring ring ring')
    def send_sms(self,number,text):
        sms = f'sending {text} to {number}'
        return sms

my_phone = Phone()
my_phone.call()
sms = my_phone.send_sms('01916044065', 'Hello')
print(sms)