def replace_word(lst, s):
    l = len(lst)
    for ind,word in enumerate(lst):
        # print(word,index)
        if ind+1 < l:
            next_word = replace_with[ind+1] 
            s = s.replace(word,next_word)
            del replace_with[ind+1]
            
            # print(next_word)
        else:
            None      
    return s


replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
sa =  replace_word(replace_with,s)
print(sa)