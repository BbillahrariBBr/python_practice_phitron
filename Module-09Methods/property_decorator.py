class User():
    def __init__(self,f_name,l_name):
        self.first = f_name
        self.second = l_name
        self.email = f'{self.first}.{self.second}@user.com'
    @property    
    def full_name(self):
        return f'{self.first} {self.second}'
    
    @full_name.setter
    def full_name(self, value):
        first, second = value.split(' ')
        self.first = first
        self.second = second
        self.email = f'{first}.{second}@user.com'
    
    @full_name.deleter
    def full_name(self):
        del self.first
        del self.second

    def get_email(self):
        return self.email

mark = User('mark','zuku')
print(mark.first)
print(mark.second)
print(mark.email)
print(mark.get_email())
print(mark.full_name)
mark.full_name = 'tom hanks'
print(mark.full_name)
print(mark.email)
# del mark.full_name
print(mark.first)
print(mark.second)