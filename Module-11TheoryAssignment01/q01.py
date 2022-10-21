def exp(a, n):
    return a ** n

a, n = input("enter numbers: ").split()
a_int = int(a)
n_int = int(n)
res = exp(a_int,n_int)
print(f'result is: {res}')