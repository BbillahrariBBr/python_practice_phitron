def reverse_word(string):
    lst = string.split()
    newString = ""
    for word in lst:
        newString += (word[::-1]) + " "
    
    return newString


s = "Programming Hero is the best"

output = reverse_word(s)   
print(output)