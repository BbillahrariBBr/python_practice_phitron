# with open('message.txt','a') as fileWrite:
#     fileWrite.write('i love python')
with open('message.txt','r') as fileRead:
    text = fileRead.read()
    print(text)