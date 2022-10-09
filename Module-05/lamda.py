# def square(x):
#     return x*x

# func_name = lambda var_name: return val or function work
square = lambda x: x*x
res = square(6)
# print(res)
add = lambda x,y : x+y
sum = add(45,56)
# print(sum)
num = [12,45,65,23,89,78,11]

def  double_it(x):
    return x*2

double_it2 = lambda x : x*3

doubled_numbers = map(lambda x: x*4 ,num)
sqr_numbers = map(lambda x: x*x ,num)
# print(list(sqr_numbers))
bigger_nm = filter(lambda n: n>50, num)
print(list(bigger_nm))