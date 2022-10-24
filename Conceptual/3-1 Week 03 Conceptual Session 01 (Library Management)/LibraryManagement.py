class User:
    
    def __init__(self,name,roll,password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = [] 
        self.returns_books = []
class Library:
    def __init__(self,book_list) -> None:
        self.book_list = book_list
    
library = Library({"English": 2, "Bangla":5,"Math":3})
allUsers = []
currentUser = None  
while True:
    if currentUser  == None:
        print("Not Logged In\n plz login or create Account(L/C)")
        option = input()
        if option == "L":
            roll = int(input("Roll: "))
            password = input("Password: ")
            match = False
            for user in allUsers:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    match = True
            if match == False:
                print("No User Found")
        else:
            name = input("name: ")
            roll = int(input("roll: "))
            password = input("Password: ")
            user = User(name,roll,password)
            currentUser = user
    else: 
        print("Options")
        print("_______")
        print("1. Borrow a book")
