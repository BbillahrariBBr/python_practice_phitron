def do_something():
    print('Inside the function do_something')
    def inner_function():
        print('inside the inner function')
    inner_function()

# do_something()

def first_fuinction():
    print('Inside the first funct')
    def second_funct():
        print('Inside the second funct')
    return second_funct

# first = first_fuinction()
# first()
# print(first)
first_fuinction()()