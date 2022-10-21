# 1,1,2,3,5,8,13,21,
# without cache Time Took 8489.630460739136
import time
from functools import cache
@cache
def fib(n):
    if n <=1:
        return 1
    return fib(n-1)+ fib(n-2)

start = time.time()
for i in range(40):
    print(i, fib(i))

end = time.time()
ms = (end- start)*1000
print('Time Took', ms)