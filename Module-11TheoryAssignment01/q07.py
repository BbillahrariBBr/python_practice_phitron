def subsets(s):
    x = len(s)
    newList = []
    for i in range(2 ** x):
        newList.append ([s[j] for j in range(x) if (i & (1 << j))])
    return newList

output = subsets([4,5,6])
print(output)

# print(1<<3)