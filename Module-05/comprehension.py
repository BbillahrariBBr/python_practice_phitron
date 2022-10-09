num = [12,45,65,23,89,78,11]

odd_num = []
for n in num:
    if n % 2 == 1:
        odd_num.append(n)

# print(odd_num)

odd = [n for n in num if n %2 == 1 if n % 5 !=0]
print(odd)
names = ['sakibs','salman', 'sabbir']
ages = [37,32,21]
pairs = [(name, age) for name in names for age in ages if age<25]
print(pairs)