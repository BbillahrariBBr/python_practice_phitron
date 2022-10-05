# prob_02.EncryptandDecrypt.py
#  ord() dile ascii value pawa jabe
#decrypt kora lagbe

data = 'firebaby'
# data = 'az'
shift = 1;
output = ''
for character in data:
    output+= chr((ord(character)+shift-97)%26+97)

print(output)
