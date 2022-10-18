def create_list(dict):
    lst = []
    for key, value in dict.items():
        # temp = [key,value]
        lst.append(key)
        lst.append(value)
    print(lst) 

x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

create_list(d)

