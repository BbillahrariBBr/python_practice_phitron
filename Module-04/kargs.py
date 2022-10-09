def full_name(f_name, l_name):
    name = f'{f_name} {l_name}'
    return name

name = full_name(l_name= 'chowdhury', f_name= 'choto')
# print(name)

def long_name(**kargs):
    print(kargs)

# long_name(first = 'Dr. ', last = 'chowdhury', middle='Rahman')

def name_mixed(f_name, l_name, **name_parts):
    print(f_name, l_name,name_parts )

# name = name_mixed(l_name= 'chowdhury', f_name= 'choto', middle='Dr.')

def all_types(firs,*args,**kargs):
    print(firs)
    for word in args:
        print(word)
    for key, value in kargs.items():
        print(value)

all_types('abd','ddd','kjk','lll','pp', k= 'kkk', m='mmm')