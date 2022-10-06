""" 
2.	Write a program to print the following number pattern using a loop.
Input : 5
Output : 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

 """

number = int(input('Enter a Number: '))
for i in range(number):
    for j in range(i+1):
        print(j+1,end=' ')
    print()

# for i in range(5):
#     for j in range(5):
#         print(j+1, end=' ')
#     print() # new line