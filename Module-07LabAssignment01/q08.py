def make_upper(text):
    s = ""
    for i in text:
        if(ord(i)>= 97  and ord(i)<=122):
            n =  ord(i)-32
            s += chr(n)
        else:
            s+=i
    return s

def make_lower(text):
    s = ""
    for i in text:
        if(ord(i)>= 65  and ord(i)<=90):
            n =  ord(i)+32
            s += chr(n)
        else:
            s+=i
    return s

def make_capital(text):
    count = 0
    s = ""
    for i in text:
        if count == 0:
            if(ord(i)>=97 and ord(i)<=122):
                n = ord(i)-32
                s += chr(n)
                count = 1
        else:
            if(ord(i)>= 65  and ord(i)<=90):
                n =  ord(i)+32
                s += chr(n)
            else:
                s+=i
    return s


def  test_script():
    text = "i am learning PYTHON."
    assert  make_capital(text) == text.capitalize()
    assert  make_upper(text) == text.upper()
    assert  make_lower(text) == text.lower()


