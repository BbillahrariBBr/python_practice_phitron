""" absolute value without library function """
# func for abs
def abslt(value):
    if(value<0):
        value = value * (-1)
    print(value)

# funct for input
def inputUser():
    value = int(input('Enter a integer value: '))
    abslt(value)

# input using function
inp = 1;
while inp<4:
    inputUser()
    inp+=1