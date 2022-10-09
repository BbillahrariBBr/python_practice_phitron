num = [12,45,65,23,89,78,11]
try:
    num_iter = iter(num)
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print('some')
    print('some thin')
    print(next(num_iter))
    print(next(num_iter))
    print('some thin')
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
except StopIteration:
    print('iteration is stoped')