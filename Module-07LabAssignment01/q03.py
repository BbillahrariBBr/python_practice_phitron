""" 
chatbot
1. input /listen
2. process/decide
3. output/talkback
 """
import pyjokes

neutral_joke = ['neutral']
chuck_joke = ['chuck']
all_joke = ['all']

def listen():
    return input("say something: ")

def decide(command):
    # print(command)
    command = command.lower()
    broken_word = command.split()
    # print(broken_word)
    for word in broken_word:
        if word in neutral_joke:
            talkback(pyjokes.get_joke(category='neutral'))
            break
        elif word in chuck_joke:
             talkback(pyjokes.get_joke(category='chuck'))
             break
        elif word in all_joke:
             talkback(pyjokes.get_joke(category='all'))
             break




def talkback(respons):
    print(respons)

while True:
    command = listen()
    decide(command)