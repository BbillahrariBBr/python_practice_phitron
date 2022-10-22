def powerset(s):
    x = len(s)
    newList = []
    for i in range(1 << x):
        newList.append ([s[j] for j in range(x) if (i & (1 << j))])
    return newList

output = powerset([4,5,6])
print(output)

# print(1<<3)