# bbbbiiUUUUUxxx
string = 'x3b4U5i2'

expanded = ''

for character in string:
    if character.isdigit():
        expanded += expanded[-1] * (int(character) - 1)
    else:
        expanded += character

print(expanded)