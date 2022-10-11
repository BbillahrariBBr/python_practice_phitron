""" 
chatbot
1. input /listen
2. process/decide
3. output/talkback
 """
greet_words = ['hi', 'hello','yo']
bye_words = ['bye','tata','hasta la vista']
bad_words = ['dog','pocha']

def listen():
    return input("say something: ")

def decide(command):
    # print(command)
    command = command.lower()
    broken_word = command.split()
    # print(broken_word)
    for word in broken_word:
        if word in greet_words:
            talkback("Hi There")
            break
        elif word in bye_words:
            talkback("Tata Bye Bye")
            break
        elif word in bad_words:
            talkback("You are a bad guy, Behave yourself")
            break




def talkback(respons):
    print(respons)

while True:
    command = listen()
    decide(command)