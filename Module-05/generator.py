num = [12,45,65,23,89,78,11]
def getNumbers(nums):
    for n in nums:
        yield n

res = getNumbers(num)
print(next(res))
print(next(res))
print(next(res))
print('some')
print('some thin')
print(next(res))
print(next(res))

print('some')
print('some thin')
print(next(res))
print(next(res))
print(next(res))