""" check number is positive or not """
print('for leave type "Quit" \n')
while True:
    inp = input('Enter input: ')
    if inp == 'Quit' or inp == 'quit':
        break
    else:
        inp_int = int(inp)
        if inp_int <0:
            print(f'{inp_int} is negative')
        elif inp_int >0:
            print(f'{inp_int} is positive')
        else:
            print(f'{inp_int} is zero')
