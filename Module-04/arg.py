from unittest import result


def add(num1,num2):
    total = num1+num2
    print(num1,num2)
    return total

# result = add(num2=12,num1=14)

def multiply(num1,num2=1):
    result = num1*num2
    return result

# print(multiply(45))

def mul(*numbers):
    print(numbers)
    result =1
    for num in numbers:
        result *= num
    # result = numbers
    return result

print(mul(1,2,3,5))
