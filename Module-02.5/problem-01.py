from locale import format_string
from math import ceil, floor


number = float(input('Enter a float Number: '))
cel = ceil(number)
flr = floor(number)
print(f'for {number} floor is {flr} and Cell is {cel}')