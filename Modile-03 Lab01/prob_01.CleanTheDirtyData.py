#  prob_01.CleanTheDirtyData.py
# chaallange holo last a e kta - ase seta na lika
data = "aNtEriOur\n\t>>"
new_data = data.lower()
output_data = ''
for character in new_data:
    if  (character == 'a') or (character == 'e') or (character == 'i') or (character == 'o') or (character == 'u'):
        output_data += character + "-"
        # print(f'{character} Found')
    # print(character)
# print(data.lower())
print(output_data)