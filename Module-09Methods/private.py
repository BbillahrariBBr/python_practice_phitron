class User:
    def __init__(self,name,password,phone):
        self.name = name
        self.__password = password
        self.__phone = phone
    
    def __get_pass(self):
        print(self.__password)

    def user_log(self,name,password):
        if(name == self.name and password  == self.__password):
            return True
        return False

ryan = User('Ryan Dal','NodeAbcd','0171456678')
# print(ryan.__password)
# print(ryan.__phone)
# ryan.__get_pass()
res = ryan.user_log('Ryan Dal','NodAbcd')
print(res)